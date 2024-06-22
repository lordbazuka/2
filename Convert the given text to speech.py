from gtts import gTTS
import os
f = open('1.txt')
x=f.read()
langauge='en'
audio=gTTS(text=x,lang=langauge)
audio.save("wishes.wav")
os.system("wishes.wav")
print("program executed succesfully.")