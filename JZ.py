import speech_recognition as sr
from googletrans import Translator
import subprocess

# Initialize recognizer
r = sr.Recognizer()

# Use microphone as audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# Use Google Speech Recognition to convert audio to text
try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))

    # Translate the text
    translator = Translator()
    translated_text = translator.translate(text, dest='es').text
    print("Translated text: {}".format(translated_text))

    # Use Voicevox to convert text to speech
    command = ['open', '-a', 'Voicevox', '--args', translated_text]
    subprocess.Popen(command)
except sr.UnknownValueError:
    print("Unable to recognize speech")
except sr.RequestError as e:
    print("Error: {}".format(e))

