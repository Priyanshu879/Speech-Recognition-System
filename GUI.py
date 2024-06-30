from tkinter import*
from PIL import Image, ImageTk
import threading
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import cv2 
import googletrans
import gtts
import playsound


root = Tk()
root.title("Voice Recognition and Translation System")
root.geometry("630x675")
root.resizable(False,False)
root.config(bg="#6F8FAF")

is_running = False

def ASK():
    

    def Say(Text):
        engine = pyttsx3.init()
        Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
        engine.setProperty('voice',Id)
        text.insert(END,"Friday-->"+Text+"\n")
        engine.say(Text)
        engine.runAndWait()

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            text.insert(END,"Listening....."+"\n") 
            
            r.pause_threshold = 1
            audio = r.listen(source,0,8)
            try:
                text.insert(END,"Recognizing....."+"\n")
                query = r.recognize_google(audio, language="en-in")
                text.insert(END,"User Said-->"+query+"\n")
                return query
            except Exception as e:
                return "Some Error Occured. Sorry from Friday"


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
        if "Hello Friday".casefold() in query:
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
            Say("Opening camera sir...")
            openCam() 
        
        # Date Time
        elif "the time" in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            print(Time)
            Say(f"Sir the time is {Time}")

        
        #translator
        elif  "Translator".casefold() in query.casefold():
            text.insert(END,"What do you want to translate sir?"+"\n")
            Say("What do you want to translate sir?")
            query = takeCommand()
            translator = googletrans.Translator()
            translate = translator.translate(query, dest="hi")
            text.insert(END,translate.text+"\n")
            converted_audio = gtts.gTTS(translate.text, lang="hi")
            converted_audio.save("audio.mp3")
            playsound.playsound("audio.mp3")
        
        
    

        #Webbrowsing
        sites = [["youtube","https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"], 
                 ["google","https://www.google.com"], ["instagram","https://www.instagram.com"],
                 ["facebook","https://www.facebook.com"],["weather","https://www.weather.com"]  ]
        for site in sites: 
            if f"Open {site[0]}".lower() in query.lower():
                Say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])




    if __name__ == '__main__':
        Say("Hello I am Friday")
        text.insert(END,"Hello I am Friday"+"\n")
        while is_running:
            query = takeCommand()
            brain(query)


main_t = threading.Thread(target=ASK)

def start():
    global is_running
    is_running = True
    main_t.start()

def stop():
    global is_running
    is_running = False


frame = LabelFrame(root, padx=100, pady= 7, borderwidth= 3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=0 , padx=20, pady=10)

text_lable = Label(frame, text="Voice Recognition and Translation System", font=("comic Sans ms", 14, "bold"), bg="#6F8FAF")
text_lable.grid(row=0, column=0, padx=20, pady=10)
image = ImageTk.PhotoImage(Image.open(r"D:\JarvisAI\assitant.png"))
image_lable = Label(frame, image=image)
image_lable.grid(row=1, column=0, pady=20)

text = Text(root, font= ('courier 10 bold'), bg="#356696")
text.grid(row= 2, column= 0)
text.place(x = 130, y = 375, width= 375, height= 180)


# entry = Entry(root, justify=CENTER)
# entry.place(x= 145, y = 500, width = 350, height = 30)

Button1 = Button(root,text = "ASK",bg="#356696", pady=16, padx=40 , borderwidth=3, relief=SOLID , command=start)
Button1.place(x=70 , y=575)
Button2 = Button(root,text = "STOP",bg="#356696", pady=16, padx=40 , borderwidth=3, relief=SOLID , command=stop)
Button2.place(x=450 , y=575)

root.mainloop()