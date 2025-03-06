# import dependencies

import os
import subprocess
import whisper
from googletrans import Translator
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip

# Step 1: Extract Audio from Video
def extract_audio(video_path, audio_path):
    command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path}"
    subprocess.run(command, shell=True)
    
# Step 2: Transcribe Audio to Text
def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Load Whisper AI model
    result = model.transcribe(audio_path)
    return result["text"]

# Step 3: Translate Text to Hindi Audio

def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, dest='hi') # Translate to Hindi
    return translation.text


