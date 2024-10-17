import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import OpenAI_Jarvis

recognizer = sr.Recognizer()


def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def processCommand(command):
    if command.lower() == "open google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
        command = r.recognize_google(audio)
    elif command.lower() == "open youtube":
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com/")
        command = r.recognize_google(audio)   
    elif "play" in command.lower()  :
        song = command.lower().split(" ")[1]
        webbrowser.open(music.music[song])
        command = r.recognize_google(audio)  
    else:
        OpenAI_Jarvis.completion["messages"][1]["content"]


while True:
    # obtain audio from the microphone
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source,timeout=2)
        command = r.recognize_google(audio)

        
        if command.lower() == "jarvis":
            speak("Yaa")
            with sr.Microphone() as source:
                print("Jaris Activated!")
                audio = r.listen(source,timeout=2)
                command = r.recognize_google(audio)
                processCommand(command)

    except Exception as e:
        print(f"Error occured {e}")

