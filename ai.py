import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import time
from vid_to_aud import converter

def sptext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        audio=r.listen(source)

        try:
            print("recognizing....")
            data=r.recognize_google(audio)
            print("you said:- ",data)
            return data
        except UnknownValueError:
            speechtx("could not recognize please try agian later")
        except RequestError:
             print("Could not request results from Google Speech Recognition service")

import pyttsx3

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)  # Fixed the typo here
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if 'ok jarvis' in sptext().lower():
        while True:
            data1=sptext().lower()
            if "your name" in data1:
                name="my name is shanti"
                speechtx(name)
            elif "old are you" in data1:
                old="im infinite year old"
                speechtx(old)
            elif "live" in data1:
                live="i live in mahi's home"
                speechtx(live)
            elif "time" in data1:
                time=datetime.datetime.now().strftime("%I:%m:%p")
                speechtx(time)
            elif "youtube" in data1:
                speechtx("opening youtube")
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                jock1=pyjokes.get_joke(language="en",category="neutral")
                print(jock1)
                speechtx(jock1)
            elif "gpt" in data1:
                speechtx("opening chat gpt")
                webbrowser.open("https://chatgpt.com/?gad_source=1&gclid=EAIaIQobChMIxqKs_Y-MiQMVdyN7Bx27vysSEAAYASAAEgILwPD_BwE")
            elif "mahi" in data1:
                mahi="she live in madicale square nagpur"
                speechtx(mahi)
            elif "convert video to audio" in data1:
                speechtx("coverting video into audio first please select the file")
                converter()        



            else:
                speechtx("thank you have a nice day om")
                break
            time.sleep(5)