//from gtts import gTTS
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

    
    except sr.UnknownValueError:
        talkToMe('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"while(talkToMe('H'))

    if 'open google' in command:
        reg_ex = re.search('open google (.*)', command)
        url = 'https://www.google.com/'
        webbrowser.open(url)
        print('Done!')
        talkToMe('Opened')
        
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            talkToMe('Opening Website')
            webbrowser.open(url)
        else:
            pass
    
    elif 'i am nitin' in command:
        talkToMe('hey how are you')
    
        elif 'same here' in command:
        talkToMe('good')

    elif 'who are you' in command:
        talkToMe('I am sam, your voice assistant')
    
    elif 'how are you' in command:
        talkToMe('good and you')
        
    elif 'remember' in command:
        reg_ex=re.search('remember (.+)', command)
        rem=reg_ex.group(1)
        print(rem)
        sql="INSERT INTO remember VALUES ('%s')" % (rem)
        cursor.execute(sql)
        db.commit()
        talkToMe('Remembered')

    elif 'remind me' in command:
        sql="SELECT * FROM remember"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
          data = row[0]
          print ("%s" % (data))
          db.commit()
        talkToMe('These are the things you told me to remember')
          
    elif 'delete' in command:
        sql="Delete from remember"
        cursor.execute(sql)
        db.commit()
        talkToMe('Deleted things you told me to remember')
        
    elif 'thank you' in command:
        talkToMe('You are Welcome')
    
    else:
        talkToMe('I don\'t know what you mean!')


talkToMe('Hey I am Sam, How can i help you')

while True:
    assistant(myCommand())
