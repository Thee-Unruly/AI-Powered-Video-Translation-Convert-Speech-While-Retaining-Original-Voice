import streamlit as st
import os
import subprocess
import whisper
from googletrans import Translator
from gtts import gTTS

def extract_audio(video_path, audio_path):
    command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path}"
    subprocess.run(command, shell=True, check=True)

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, dest='hi')
    return translation.text

def text_to_speech(text, hindi_audio_path):
    speech = gTTS(text=text, lang='hi', slow=False)
    speech.save(hindi_audio_path)

def merge_video_and_speech(video_path, hindi_audio_path, output_video_path):
    command = f"ffmpeg -i {video_path} -i {hindi_audio_path} -c:v copy -c:a aac {output_video_path}"
    subprocess.run(command, shell=True, check=True)

st.title("AI-Powered Video Translation")
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    video_path = "uploaded_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("Video uploaded successfully!")

    audio_file = "audio.wav"
    translated_audio = "translated_audio.mp3"
    output_video = "output_translated.mp4"

    if st.button("Translate Video to Hindi"):
        try:
            st.text("Extracting audio...")
            extract_audio(video_path, audio_file)

            st.text("Transcribing audio...")
            text = transcribe_audio(audio_file)

            st.text("Translating text to Hindi...")
            translated_text = translate_to_hindi(text)

            st.text("Generating Hindi speech...")
            text_to_speech(translated_text, translated_audio)

            st.text("Merging translated audio with video...")
            merge_video_and_speech(video_path, translated_audio, output_video)

            st.success("Translation complete! Download your video below.")
            st.video(output_video)
            st.download_button("Download Translated Video", output_video, file_name="translated_video.mp4")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
