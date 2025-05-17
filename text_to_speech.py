import pyttsx3 as pt

word= input('type in a word: ')

engine = pt.init()

engine.say(word)

engine.runAndWait()