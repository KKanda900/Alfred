import speech_recognition as sr
from gtts import gTTS
import sys
import traceback
import os
import googlesearch
from playsound import playsound
import webbrowser
import time
import re
import pyttsx3
import warnings

print(os.listdir('.'))

warnings.filterwarnings('ignore')


def wakeWord(text):
    WAKE_WORDS = ['alfred', 'hey alfred', 'hello alfred', 'yo alfred']
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


""" def assistant(text):
    # print(text)
    myobj = gTTS(text=text, lang='en-GB', slow=False)
    text = re.sub('[? ]+', '', text)
    text = text + ".mp3"
    myobj.save(text)
    playsound(text) """

def assistant(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

""" def Test():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice, voice.id)
        engine.setProperty('voice', voice.id[0])
        engine.say("Hello World!")
        engine.runAndWait()
        engine.stop() """


def gQuery(text):
    url = "https://www.google.com.tr/search?q={}".format(text)
    webbrowser.open_new_tab(url)


def searchWeather(text):
    url = "https://www.google.com/search?q=weather+in+{}".format(text)
    webbrowser.open_new_tab(url)

# This definition will define all the actions needed by "alfred"


def main():
    time.sleep(3)
    audio = recordAudio()
    while wakeWord(audio):
        assistant("Whats on your mind?")
        print("Listening...")  # Just to clarify in test that it is listening
        audio = recordAudio()
        # print(audio)
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
            pass
            main()
        


if __name__ == "__main__":
    main()
    sys.stdout.flush()
