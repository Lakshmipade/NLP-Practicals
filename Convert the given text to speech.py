# Import required libraries
from gtts import gTTS
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Text and language for the TTS conversion
mytext = "Welcome to Natural Language programming"
language = "en"

# Create gTTS object
myobj = gTTS(text=mytext, lang=language, slow=False)

# Save the audio file
myobj.save("myfile.mp3")

# Load and play the audio file
pygame.mixer.music.load("myfile.mp3")
pygame.mixer.music.play()

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    time.sleep(1)
