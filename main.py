import speech_recognition as sr
import pyttsx3


Listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Eu Sou sua Alexa')
engine.say('O que posso fazer Por você')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = Listener.listen(source)
        command = Listener.Recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except: 
    pass


##altera~ção feita por mim