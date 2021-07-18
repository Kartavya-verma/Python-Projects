import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening") 
    speak("I am Jarvis Sir.Please tell me how may I help you") 

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to,content):
#     server =smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com','your-password')
#     server.sendmail('yourgmail.com.com',to,content)




if __name__ == "__main__":
    # speak("A B C D E H I J K L M N O P Q R S T U V W X Y Z")
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir='D:\\Non Critical\\songs\\Favorite Songs'
        #     songs=os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strfTime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        
        elif 'open code' in query:
            codepath="C:\\Users\\Kartavya Verma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        # elif 'email to kartavya' in query:
        #     try:
        #         speak("What should I say?")
        #         content=takeCommand()
        #         to="vermakartavya2000@gmail.com"
        #         sendEmail(to,content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry KV.I am not able to send this mail!!")
        
        elif 'exit' in query:
            exit()
