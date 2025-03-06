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
    
# Give it a web interactive interface for testing purposes
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
        extract_audio(video_path, audio_file)
        text = transcribe_audio(audio_file)
        translated_text = translate_to_hindi(text)
        text_to_speech(translated_text, translated_audio)
        merge_video_and_speech(video_path, translated_audio, output_video)
        
        st.success("Translation complete! Download your video below.")
        st.video(output_video)
        st.download_button("Download Translated Video", output_video, file_name="translated_video.mp4")