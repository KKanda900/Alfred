import sys, traceback, os, googlesearch, webbrowser, time, re, pyttsx3, warnings
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

warnings.filterwarnings('ignore')

def wakeWord(text):
    WAKE_WORDS = ['alfred', 'hey alfred', 'hello alfred', 'yo alfred', 'I need help', 'can you help me with this?']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

def endSession(text):
    END_WORDS = ['end', 'stop alfred', 'thats it']
    text = text.lower()
    for phrase in END_WORDS:
        if phrase in text:
            return True

    return False

def weatherVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        assistant("What location do you want the weather for?")
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio)
        #print("You said: " + data)
    except Exception as e:
        print("Lets try again")
        recordAudio()

    data = data.lower()
    return data

def jot_down_task():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        assistant("What did you want me to write down for you?")
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio)
        #print("You said: " + data)
    except Exception as e:
        print("Lets try again")
        recordAudio()

    data = data.lower()
    return data

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        assistant("Hey how can I help you today?")
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio)
        #print("You said: " + data)
    except Exception as e:
        print("Lets try again")
        recordAudio()

    data = data.lower()
    return data


def assistant(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def gQuery(text):
    url = "https://www.google.com.tr/search?q={}".format(text)
    webbrowser.open_new_tab(url)

def searchWeather(text):
    url = "https://www.google.com/search?q=weather+in+{}".format(text)
    webbrowser.open_new_tab(url)

def main():
    audio = recordAudio()
    while wakeWord(audio):
        assistant("Welcome Karun! How may I be assistance to you?")
        print("Listening...")  # Just to clarify in test that it is listening
        audio = recordAudio()
        if(endSession(audio)):
            assistant("Good bye")
            sys.exit(0)
        if("search" in audio):
            audio = audio[6:len(audio)]
            gQuery(audio)
            main()
        elif("open" in audio):
            audio = audio[4:len(audio)]
            os.startfile(audio)
            main()
        elif("howstheweather" in audio):  # This is temporary
            location = weatherVoice()
            searchWeather(location)
            main()
        elif("jot down" in audio):
            task = jot_down_task()
            f = open("../Data/tasks.txt", "a")
            f.write("Noted Task:" + " " + task + "\n\n")
            f.close()
        else:
            break

if __name__ == "__main__":
    main()
    sys.stdout.flush()