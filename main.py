# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Ruchi! I am Jarvis how may I help you")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Ruchi!I am Jarvis how may I help you")   

    else:
        speak("Good Evening Ruchi ! I am Jarvis how may I help you")  

           

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":

    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "let's shop" in query:
            webbrowser.open("amazon.com")  

        elif 'open github' in query:
            webbrowser.open("https://github.com/ruchitav64") 

        elif 'tell me a fact' in query:
            response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
            fact = response.json()['text']
            speak(f"Did you know? {fact}")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Ruchita\\Music' #add the path to your music folder/directory
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f", the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\RUCHITA VERMA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Ruchi' in query: #will work when you specify your email and password in the sendEmail() function above
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "example@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Ruchi. I am not able to send this email")   

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye Ruchi.")
            break
 
        else:
            print("No query matched")