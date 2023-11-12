# AI Voiceover with GPT4V

This Streamlit application demonstrates the use of AI and machine learning to automate the process of generating voiceovers for videos. 
Process video, generate narratives based on the video content, convert the narratives to audio, and then merge the audio back into the video.

# Demo

### Input Video
https://github.com/martintmv-git/gpt4v-streamlit-voiceover/assets/101264514/388d20c1-e61d-4f50-8641-4217886e2047

### Output Video
https://github.com/martintmv-git/gpt4v-streamlit-voiceover/assets/101264514/1aeb3caf-443d-4e94-abf1-4a9cf795fafb

## Features

- **Video Processing**: Converts a video into frames using OpenCV.
- **Narrative Generation**: Utilizes OpenAI's GPT-4 Vision model to create stories or scripts based on the video frames.
- **Voiceover Generation**: Converts the generated text into a voiceover using OpenAI's text-to-speech API.
- **Audio and Video Merging**: Combines the generated voiceover with the original video.

## Workflow

1. **Load Environment Variables**: Loads necessary API keys and configurations from `.env.local`.
2. **Video to Frames**: Converts an uploaded video into individual frames and encodes them in base64 format for processing.
3. **Frames to Script**: Sends the video frames to OpenAI's GPT-4 Vision model to generate a narrative or script based on the content of the frames.
4. **Text to Audio**: Converts the generated narrative into an audio file (voiceover) using OpenAI's text-to-speech service.
5. **Merge Audio and Video**: Combines the original video with the generated voiceover to create a final product.
6. **Streamlit UI**: Provides a user interface to upload videos, select voice options, and display the processed video.

## Usage

- Set up the environment by placing the OpenAI API key in `.env.local`.
- Run the Streamlit application.
- Upload a video and select a voice type.
- Generate a voiceover and view the processed video.

## Dependencies

- `dotenv`: For loading environment variables.
- `moviepy`: For video and audio processing.
- `cv2` (OpenCV): For handling video frames.
- `openai`: For accessing OpenAI's GPT-4 and text-to-speech APIs.
- `requests`: For making HTTP requests to the OpenAI API.
- `streamlit`: For creating the web-based UI.
- `tempfile`: For handling temporary files during processing.

## Requirements

- An OpenAI API key is required.
- Python 3.x and the above-mentioned libraries.

## Disclaimer

This project is for demonstration purposes and shows the capabilities of integrating AI models with video and audio processing in Python.
