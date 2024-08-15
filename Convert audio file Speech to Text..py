import speech_recognition as sr
import os

# Update the path to your file
filename = "D:/NLP-ZAMA/p1.wav"

# Check if the file exists
if not os.path.exists(filename):
    print(f"Error: The file {filename} does not exist.")
else:
    # Initialize the recognizer
    r = sr.Recognizer()

    try:
        # Open the file with sr.AudioFile
        with sr.AudioFile(filename) as source:
            # Listen for the data (load audio to memory)
            audio_data = r.record(source)
            # Recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            print(text)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except PermissionError as e:
        print(f"Permission Error: {e}")
