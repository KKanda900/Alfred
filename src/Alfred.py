import sys, traceback, os, googlesearch, webbrowser, time, re, pyttsx3, warnings, nltk
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from nltk import *
from nltk.corpus import stopwords

warnings.filterwarnings('ignore') # Filters out any warnings (shouldn't be utilized in the program every time) => just situational

# Wake words to identify to start the process
def wakeWord(text):
    WAKE_WORDS = ['alfred', 'hey alfred', 'hello alfred',
                  'yo alfred', 'I need help', 'can you help me with this?']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

# End words to end session
def endSession(text):
    END_WORDS = ['end', 'stop alfred', 'thats it']
    text = text.lower()
    for phrase in END_WORDS:
        if phrase in text:
            return True

    return False

# Returns the string of the city you want the weather for
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

# Returns a string of the task/note you want to jot down
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
    f = open("../Data/tasks.txt", "a")
    f.write("Noted Task:" + " " + data + "\n\n")
    f.close()

# Uses Google TTS to returns a string of what the user said
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

# Enables the Assistant to speak back to the user


def assistant(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Allows to output a google search of what the user wanted to search up


def gQuery(text):
    url = "https://www.google.com.tr/search?q={}".format(text)
    webbrowser.open_new_tab(url)

# Allows to output a Google Weather Report of the Requested City


def searchWeather(text):
    url = "https://www.google.com/search?q=weather+in+{}".format(text)
    webbrowser.open_new_tab(url)

# This is where the Alfred process initiates from


def main():
    audio = recordAudio()
    while wakeWord(audio):
        assistant("Welcome Karun! How may I be assistance to you?")
        print("Listening...")  # Just to clarify in test that it is listening
        audio = recordAudio()  # Records audio from the user
        tokens = word_tokenize(text)  # tokenizes the sentence to find keywords
        sWords = set(stopwords.words('english'))  # removes stopwords
        cleanTokens = [w for w in tokens if not w in sWords]
        tagged = nltk.pos_tag(cleanTokens)  # creates tags for the sentences
        # This is where the word is being processed and Alfred will output the accurate response back
        if(endSession(audio)):
            assistant("Good bye")
            sys.exit(0)
        if(tagged.contains("search")):
            audio = audio[6:len(audio)]
            gQuery(audio)
            main()
        elif(tagged.contains("open")):
            audio = audio[4:len(audio)]
            os.startfile(audio)
            main()
        elif(tagged.contains("weather")):  # This is temporary
            location = weatherVoice()
            searchWeather(location)
            main()
        elif(tagged.contains("jot down")):
            jot_down_task()

        else:
            break


# Start/Initiate Method
if __name__ == "__main__":
    main()
    sys.stdout.flush()
