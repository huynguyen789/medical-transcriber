
# # UPLOAD FILE:
# #######################################################
# audio_file = st.file_uploader("Choose an audio file", type=['wav', 'mp3', 'mp4'])

# #Transcribe
# model = whisper.load_model('tiny.en')
# transcribed_text = ""
# if audio_file is not None:
#     with st.spinner('Generating transcription...'):
#         with tempfile.NamedTemporaryFile() as tmp:
#             tmp.write(audio_file.read())

#             result = model.transcribe(tmp.name, fp16=False)
#             transcribed_text = result['text']
#             # print(text)
#             st.text_area("Transcribed text:", value=transcribed_text, height=200)
# #######################################################

