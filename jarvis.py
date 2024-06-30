import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import cv2 
import openai
from config import apikey


speaker = win32com.client.Dispatch("SAPI.SpVoice")

def Say(text):
    speaker.Speak(f"{text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....") 
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"

chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    Say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def openCam():
    # define a video capture object 
    vid = cv2.VideoCapture(0) 
    
    while(True): 
        
        # Capture the video frame 
        # by frame 
        ret, frame = vid.read() 
    
        # Display the resulting frame 
        cv2.imshow('frame', frame) 
        
        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    
    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows() 


if __name__ == '__main__':
    Say("Hello I am Jarvis AI")
    while True:
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"], ["google","https://www.google.com"], ["instagram","https://www.instagram.com"] ]
        for site in sites: 
            if f"Open {site[0]}".lower() in query.lower():
                Say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # Music
        if "Open music".casefold() in query:
            os.system(r"E:\b\baller.mp3")

        # Camera
        if "Open camera".casefold() in query:
            openCam()    
            
        # Date Time
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            Say(f"Sir the time is {strfTime}")
        
        else:
            chat(query)

        # Say(query) 