# AI Voiceover with GPT4V

This Streamlit application, along with a Jupyter notebook implementation, demonstrates the use of AI and machine learning to automate the process of generating voiceovers for videos. The solution involves processing video, generating narratives based on the video content, converting the narratives to audio, and then merging the audio back into the video for a complete voiceover experience.

## Demo

### Input Video
[Input Video](https://github.com/martintmv-git/gpt4v-streamlit-voiceover/assets/101264514/388d20c1-e61d-4f50-8641-4217886e2047)

### Output Video
[Output Video](https://github.com/martintmv-git/gpt4v-streamlit-voiceover/assets/101264514/1aeb3caf-443d-4e94-abf1-4a9cf795fafb)

### Jupyter Notebook
<img width="1680" alt="Screenshot 2024-01-30 at 13 52 29" src="https://github.com/martintmv-git/gpt4v-streamlit-voiceover/assets/101264514/a8f05ef6-79b1-40ad-9998-8d52b424c1c5">

## Features

- **Video Processing**: Converts a video into frames using OpenCV.
- **Narrative Generation**: Utilizes OpenAI's GPT-4 Vision model to create stories or scripts based on the video frames.
- **Voiceover Generation**: Converts the generated text into a voiceover using ElevenLabs's text-to-speech API.
- **Audio and Video Merging**: Combines the generated voiceover with the original video, extending or trimming the video as needed to match the voiceover duration.

## Workflow

1. **Environment Setup**: Load necessary API keys and configurations.
2. **Video to Frames**: Convert a video into individual frames suitable for AI processing.
3. **AI-Generated Script**: Use OpenAI's GPT-4 model to create a script based on the video frames.
4. **Text to Speech**: Convert the script to audio with OpenAI's or ElevenLabs's TTS service.
5. **Video Finalization**: Merge the audio back into the video, adjusting the video duration to match the audio if necessary.

## Jupyter Notebook Implementation

The Jupyter notebook `voiceover_jupyter-notebook.ipynb` includes the full implementation of the AI voiceover process:

- **Extracting Video Frames**: Load a video file and extract frames as base64-encoded images.
- **AI Script Generation**: Send the frames to OpenAI's GPT-4 model to generate a voiceover script.
- **Text-to-Speech Conversion**: Convert the script into a voiceover audio file using OpenAI's or ElevenLabs's TTS service.

The notebook provides a step-by-step guide, complete with code and markdown explanations, to illustrate the entire process of creating an AI-generated voiceover for video content.

## Dependencies

- `python-dotenv`: For loading environment variables.
- `moviepy`: For video and audio processing.
- `opencv-python`: For handling video frames.
- `openai`: For accessing OpenAI's GPT-4 API.
- `requests`: For making HTTP requests to the TTS API.
- `streamlit`: For creating the web-based UI (for the Streamlit app).

## Requirements

- An OpenAI API key and/or ElevenLabs API key are required.
- Python 3.x and the above-mentioned libraries.

## Disclaimer

This project is for demonstration purposes and showcases the integration of AI models with video and audio processing in Python, using both a Streamlit app and a Jupyter Notebook.
