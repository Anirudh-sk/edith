import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning Anirudh!')
    elif hour>=12 and hour<17:
        speak('good afternoon anirudh!')
    else :
        speak('good evening anirudh!')
    speak(" i am edith . How can i help you")

def microinput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.energy_threshold=50
        audio=r.listen(source)

    try:
        print('recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f'user said : {query} \n')
        speak(f'do you want me to search {query} in the web')
        if 'yes' in query :
            speak('searching ....')
            print('searching....')

    except Exception as e:
        # print(e)
        speak('can you please speak up....')
        print('can you please speak up....')
        return "None"
    return query

def sendmail(to,content):
    server=smtplib.SMTP('smpt.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('amazinganirudhhere@gmail.com','ok')
    server.sendmail('amazinganirudhhere@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    greet()
    while True:
        query=microinput().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open gmail' in query:
            webbrowser.open('www.gmail.com')

        elif 'play music' in query:
            music_dir='D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'the time is {time}')
            print(time)

        elif 'comand prompt' in query:
            path="C:\\Windows\\system32\\cmd.exe"
            os.startfile(path)

        elif 'email' in query:
            try:
                speak('what should i mail ?')
                content=microinput()
                to='anirudhsk30@gmail.com'
                sendmail(to,content)
                speak('email sent successfully!!')
            except Exception as e:
                print(e)
                speak('unable to send email now !!')
                print('email was not sent')

        elif "what\'s up" in query or 'how are you' in query:
            Msgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            speak(random.choice(Msgs))

        elif 'quit' in query:
            speak("have a great day!!")
            exit()
