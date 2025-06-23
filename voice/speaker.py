import pyttsx3

engine = pyttsx3.init()

def say(texto):
    engine.say(texto)
    engine.runAndWait()
