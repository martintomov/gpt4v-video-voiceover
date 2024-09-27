from IPython.display import display, Image, Audio
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

import cv2
import base64
import io
import openai
import os
import requests
import streamlit as st
import tempfile

## 1. Turn video into frames
def video_to_frames(video_file):
    # Save the uploaded video file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmpfile:
        tmpfile.write(video_file.read())
        video_filename = tmpfile.name
    
    video_duration = VideoFileClip(video_filename).duration
    video = cv2.VideoCapture(video_filename)
    base64Frame = []
    
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        base64Frame.append(base64.b64encode(buffer).decode("utf-8"))
    
    video.release()
    print(len(base64Frame), "frames read.")
    return base64Frame, video_filename, video_duration

## 2. Generate stories based on frames with gpt4v
def frames_to_story(base64Frames, prompt, api_key):
    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                prompt,
                *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::50]),
            ],
        },
    ]
    params = {
        "model": "gpt-4o-mini",
        "messages": PROMPT_MESSAGES,
        "api_key": api_key,
        "headers": {"Openai-Version": "2020-11-07"},
        "max_tokens": 500,
    }
    result = openai.ChatCompletion.create(**params)
    print(result.choices[0].message.content)
    return result.choices[0].message.content

## 3. Generate voiceover from stories
def text_to_audio(text, api_key, voice):
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": "tts-1",
            "input": text,
            "voice": voice,
        },
    )
    
    if response.status_code != 200:
        raise Exception("Request failed with status code")
    
    audio_bytes_io = io.BytesIO()
    for chunk in response.iter_content(chunk_size=1024*1024):
        audio_bytes_io.write(chunk)
    audio_bytes_io.seek(0)
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        for chunk in response.iter_content(chunk_size=1024*1024):
            tmpfile.write(chunk)
        audio_filename = tmpfile.name
    
    return audio_filename, audio_bytes_io

## 4. Merge videos & audio
def merge_audio_video(video_filename, audio_filename, output_filename):
    print("Merging audio and video ...")
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_filename, codec='libx264', audio_codec="aac")
    video_clip.close()
    audio_clip.close()
    
    return output_filename

## 5. Streamlit UI
def main():
    st.set_page_config(page_title="AI Voiceover", page_icon="🔮")
    st.title("GPT4V AI Voiceover 🎥🔮")
    openai_key = st.text_input("Enter your OpenAI API key")
    
    if not openai_key:
        st.error("Please enter your OpenAI API key.")
        return
    
    uploaded_file = st.file_uploader("Select a video file", type=["mp4", "avi"])

    option = st.selectbox(
        'Choose the voice you want',
        ('Female Voice', 'Male Voice'))
    classify = 'alloy' if option == 'Male Voice' else 'nova'

    if uploaded_file is not None:
        st.video(uploaded_file)
        p = 'Generate a short voiceover script for the video, matching the content with the video scenes. The style should be...'
        prompt = st.text_area("Prompt", value=p)
    
    if st.button("START PROCESSING", type="primary") and uploaded_file is not None:
        with st.spinner("Video is being processed..."):
            base64Frame, video_filename, video_duration = video_to_frames(uploaded_file)
            est_word_count = video_duration * 4
            final_prompt = f"{prompt}(This video is ONLY {video_duration} seconds long. So make sure the voiceover MUST be able to be explained in less than {est_word_count} words. Ignore and don't generate anything else than the script that you'll use to voice over the video.)"
            text = frames_to_story(base64Frame, final_prompt, openai_key)
            st.write(text)
            audio_filename, audio_bytes_io = text_to_audio(text, openai_key, classify)
            output_video_filename = os.path.splitext(video_filename)[0] + "_output.mp4"
            final_video_filename = merge_audio_video(video_filename, audio_filename, output_video_filename)
            st.video(final_video_filename)
            os.unlink(video_filename)
            os.unlink(audio_filename)
            os.unlink(final_video_filename)

if __name__ == "__main__":
    main()