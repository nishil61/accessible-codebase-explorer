# main.py

import os
import pygame
from uuid import uuid4
from tts_engine import text_to_speech, save_speech
from stt_engine import speech_to_text

def initialize_pygame_mixer():
    try:
        # Attempt to initialize the mixer
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Warning: Failed to initialize audio device. {e}")
        # Set the environment variable for SDL to use the dummy audio driver
        os.environ['SDL_AUDIODRIVER'] = 'dummy'
        # Reinitialize the mixer with the dummy driver
        pygame.mixer.init()

def main():
    choice = input("Do you want to convert text to speech or speech to text? (tts/stt): ")
    if choice == 'tts':
        text = input("Enter the text you want to convert to speech: ")
        language = input("Enter the language code (e.g., 'en' for English): ")
        tts = text_to_speech(text, lang=language)
        
        # Generate a unique filename for the audio file
        unique_filename = f"speech_{uuid4()}.mp3"
        audio_path = os.path.join('audio_files', unique_filename)
        
        # Save the speech to an audio file
        save_speech(tts, audio_path)
        
        # Initialize pygame mixer
        initialize_pygame_mixer()
        
        # Load the audio file
        pygame.mixer.music.load(audio_path)
        
        # Play the audio file
        print("Playing the speech...")
        pygame.mixer.music.play()
        
        # Keep the program running until the audio has finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif choice == 'stt':
        audio_path = input("Enter the path to the audio file for speech-to-text conversion: ")
        speech_to_text(audio_path)

if __name__ == "__main__":
    main()
