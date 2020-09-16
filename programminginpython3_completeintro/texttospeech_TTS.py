from gtts import gTTS
import os
import playsound

mytext = 'Welcome to Ford Motors Company! This is Text To Speech Services. Today is Wednesday.'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Hello_tts1dk.mp3")
playsound.playsound("Hello_tts1dk.mp3", True)
