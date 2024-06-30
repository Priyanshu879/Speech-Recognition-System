import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import cv2 
import googletrans
import gtts
import playsound

def Say(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Bravo AI : {text}")
    print("")
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("")
        print("Listening.....") 
        print("")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said : {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"


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

def brain(query):
    if "Hello bravo".casefold() in query:
        Say("Hello Sir, Welkcome Back!")

    if "Bye".casefold() in query:
        Say("Nice to Meet you Sir, Bye")
        
    # Music
    elif f"play music".casefold() in query:
        music_dir = r'E:\b'
        songs = os.listdir(music_dir)
        print(songs)
        Say(f"Playing music sir....")
        os.startfile(os.path.join(music_dir, songs[1]))
    
    # Camera
    elif "Open camera".casefold() in query:
        openCam() 
    
    # Date Time
    elif "the time" in query:
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        print(Time)
        Say(f"Sir the time is {Time}")

    
    #translator
    elif "translater".casefold() in query:
        Say("What do you want to translate sir?")
        query = takeCommand()
        translator = googletrans.Translator()
        translate = translator.translate(query, dest="hi")
        print(translate.text)
        converted_audio = gtts.gTTS(translate.text, lang="hi")
        converted_audio.save("audio.mp3")
        playsound.playsound("audio.mp3")
        


    #Webbrowsing
    sites = [["youtube","https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"], ["google","https://www.google.com"], ["instagram","https://www.instagram.com"],["facebook","https://www.facebook.com"],  ]
    for site in sites: 
        if f"Open {site[0]}".lower() in query.lower():
            Say(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])




if __name__ == '__main__':
    Say("Hello I am Bravo AI")
    while True:
        query = takeCommand()
        brain(query)