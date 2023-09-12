Here is a README file for the code:

```python
# Doctor's Assistant

This is a Streamlit app that allows users to record audio, transcribe it, and generate a summary. It uses the following main libraries:

- streamlit
- st_audiorec
- whisper
- anthropic

## Functionality

The app has the following functionality:

- Record audio using st_audiorec
- Save the audio to a wav file
- Transcribe the audio using Whisper's speech recognition 
- Summarize the transcribed text using Anthropic's Claude AI
- Display the transcribed text and summary


## Usage

To use the app:

1. Run `streamlit run app.py`
2. Click the 'Record Audio' button to record audio through the microphone
3. Once completed, click 'Generate Transcription' to transcribe the audio using Whisper 
4. Click 'Generate Summary' to summarize the transcribed text using Claude
5. The transcribed text and summary will be displayed

## Configuration

The following environment variables need to be set:

- `CLAUDE_API_KEY`: Get your API key from Anthropic and set as a Streamlit secret

## Libraries

- streamlit: Framework for building web apps in Python
- st_audiorec: Streamlit component for recording audio
- whisper: Speech recognition model from OpenAI
- anthropic: Python client for Claude API


```
