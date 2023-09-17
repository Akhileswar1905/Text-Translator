from flask import Flask, request, render_template, jsonify
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process_audio", methods=["POST"])
def process_audio():
    try:
        audio = request.files["audio"]
        if audio:
            r = sr.Recognizer()
            with sr.AudioFile(audio) as source:
                audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            tts = gTTS(text)
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
                temp_filename = temp_file.name
                tts.save(temp_filename)
            return jsonify({"text": text, "audio_url": temp_filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
