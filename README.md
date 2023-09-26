# Medical Transcription App

This is a GUI application for medical transcription using speech recognition. It allows users to record audio, transcribe it, and generate a summary.

## Functionality

- Record audio by clicking the microphone button 
- Timer shows length of recording
- Transcribe audio using Whisper speech recognition
- Summarize transcribed text using Claude AI
- Save transcription and summary to .txt file
- Delete audio file after transcription
- Update GUI with status messages 

## Libraries

- tkinter - For creating the GUI
- pyaudio - Record audio from microphone
- whisper - OpenAI speech recognition
- anthropic - Claude AI summarization 
- wave - Save audio as .wav file
- os - File management
- threading - Run recording asynchronously 

## Usage

1. `pip install requirements.txt`
2. Add Claude API key to config.py
3. Run `python medical_transcriber.py`
4. Click mic button to start recording
5. Audio will be transcribed and summarized after stopping
6. .txt file with transcription saved in /transcribedText folder

## Improvements

- Add ability to upload audio files
- Split transcription into sections
- Highlight summary keywords in full text
- Export/email .txt file
- Add speaker diarization


