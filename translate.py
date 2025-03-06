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

# Step 4: Convert Hindi Text to Speech
def text_to_speech(text, hindi_audio_path):
    speech = gTTS(text=text, lang='hi', slow=False)
    speech.save(hindi_audio_path)
    
# Step 5: Merge Video and Hindi Speech
def merge_video_and_speech(video_path, hindi_audio_path, output_video_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(hindi_audio_path)
    merged_clip = video_clip.set_audio(audio_clip)
    merged_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")


