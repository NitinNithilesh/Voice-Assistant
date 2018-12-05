from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        talkToMe('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open google' in command:
        reg_ex = re.search('open google (.*)', command)
        url = 'https://www.google.com/'
        webbrowser.open(url)
        print('Done!')
        talkToMe('Opened')

    
    elif 'i am nitin' in command:
        talkToMe('hey how are you')
    
    else:
        talkToMe('I don\'t know what you mean!')


talkToMe('Hey I am Sam, How can i help you')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
