# AI Voiceover with GPT4V

### Hugging Face Space

[huggingface.co/spaces/martintomov/gpt4v-voiceover](https://huggingface.co/spaces/martintomov/gpt4v-voiceover)

### Input Video

[Input Video](https://github.com/martintmv-git/gpt4v-streamlit-voiceover/assets/101264514/388d20c1-e61d-4f50-8641-4217886e2047)

### Output Video

[Output Video](https://github.com/martintmv-git/gpt4v-streamlit-voiceover/assets/101264514/1aeb3caf-443d-4e94-abf1-4a9cf795fafb)

### Jupyter Notebook

[gpt4v-video-voiceover/voiceover.ipynb](https://github.com/martintomov/gpt4v-video-voiceover/blob/main/voiceover.ipynb)

## Workflow

1. **Environment Setup**: Load necessary API keys and configurations.
2. **Video to Frames**: Convert a video into individual frames suitable for processing.
3. **AI-Generated Script**: Use gpt4v to create a script based on the video frames.
4. **Text to Speech**: Convert the script to audio.
5. **Video Finalization**: Merge the audio back into the video, adjusting the video duration to match the audio if necessary.

## Requirements

- Python 3.x
- python-dotenv
- moviepy
- opencv-python
- openai
- requests
- streamlit

## Disclaimer

This project is only for demonstration and showcases purposes. Feel free to clone and modify the code to suit your needs.
