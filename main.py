from typing import Text
import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('final.wav') as source:
    audio = r.listen(source)
    try:
        Text = r.recognize_google(audio)
        print('working......')
        print(Text)
    except:
        print('pls run again')