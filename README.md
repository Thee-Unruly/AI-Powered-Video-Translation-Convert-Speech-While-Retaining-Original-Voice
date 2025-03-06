🎥 AI-Powered Video Translation 🎙️🔁🇮🇳
📌 Overview
This project enables automatic speech translation from any language to Hindi while preserving the original speaker’s voice. It takes a video as input, extracts the audio, translates the speech, and generates a new video with the translated audio while keeping the original tone and style.

🚀 Features

🎤 Speech Recognition: Detects spoken language in the video
🌍 Language Translation: Converts speech to Hindi
🎙️ Voice Cloning: Maintains the speaker's original voice
🎥 Video Processing: Outputs a new video with the translated audio
🛠️ Technologies Used

Whisper (for speech recognition)
OpenAI or Google Translate API (for translation)
ElevenLabs or Coqui TTS (for voice cloning)
FFmpeg (for video/audio processing)

📂 Installation
Clone the repository:

git clone https://github.com/Thee-Unruly/AI-Powered-Video-Translation-Convert-Speech-to-Hindi-While-Retaining-Original-Voice

cd video-translation
Install dependencies:

pip install -r requirements.txt

🎬 Usage
Run the script with an input video:

bash
Copy
Edit
python translate_video.py --input video.mp4 --output translated_video.mp4
📌 Future Improvements
Add support for multiple output languages
Improve voice cloning accuracy
Optimize real-time translation
📜 License
This project is open-source under the MIT License.

👨‍💻 Contributions are welcome! 🚀 If you have ideas or improvements, feel free to submit a pull request.