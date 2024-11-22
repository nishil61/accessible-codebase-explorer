from flask import Flask, request, jsonify
from tts_engine import text_to_speech, save_speech
from stt_engine import speech_to_text
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def handle_tts():
    text = request.form['text']
    lang = request.form['lang']
    tts = text_to_speech(text, lang)
    path = f"speech_{uuid4()}.mp3"
    save_speech(tts, path)
    return jsonify({'message': 'Success', 'path': path})

@app.route('/stt', methods=['POST'])
def handle_stt():
    audio_file = request.files['audio']
    text = speech_to_text(audio_file)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
