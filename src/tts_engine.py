# tts_engine.py

from gtts import gTTS
import os

def text_to_speech(text, lang='en', slow=False):
    """Convert text to speech."""
    tts = gTTS(text=text, lang=lang, slow=slow)
    return tts

def save_speech(tts, path):
    """Save the speech to a file."""
    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tts.save(path)
