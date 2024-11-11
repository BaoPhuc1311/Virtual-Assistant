import eel
import pyttsx3
import time
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 125)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        eel.DisplayMessage("Listening...")
        audio = r.record(source, duration=5)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def all_command(message=1):
    if message == 1:
        query = take_command()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import playYouTube
            playYouTube(query)
        else:
            print("Not run!")
    except:
        print("Error")

    eel.ShowHood()
