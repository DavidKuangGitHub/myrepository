"""speechRecognition_hw.py"""
import speech_recognition as sr

r = sr.Recognizer()
"""harvard = sr.AudioFile('harvard.wav')"""
harvard = sr.AudioFile('jackhammer.wav')
with harvard as source:
    audio = r.record(source)
print(r.recognize_google(audio))
