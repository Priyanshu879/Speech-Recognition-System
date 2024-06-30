import tkinter as tk
from tkinter import messagebox
from threading import Thread
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import cv2
import googletrans
import gtts
import playsound

class AssistantGUI:
    def _init_(self, master):
        self.master = master
        master.title("Bravo AI")

        self.label = tk.Label(master, text="Bravo AI - Voice Assistant", font=("Arial", 18))
        self.label.pack()

        self.command_entry = tk.Entry(master, width=50)
        self.command_entry.pack()

        self.listen_button = tk.Button(master, text="Listen", command=self.listen_thread)
        self.listen_button.pack()

        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.pack()

    def listen_thread(self):
        Thread(target=self.listen).start()

    def listen(self):
        query = self.takeCommand()
        self.brain(query)

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.output_text.insert(tk.END, "\nListening.....\n")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 8)
            try:
                self.output_text.insert(tk.END, "Recognizing.....\n")
                query = r.recognize_google(audio, language="en-in")
                self.output_text.insert(tk.END, f"User Said : {query}\n")
                return query
            except Exception as e:
                self.output_text.insert(tk.END, "Some Error Occurred. Sorry from Jarvis\n")

    def Say(self, text):
        engine = pyttsx3.init()
        Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        engine.setProperty('voice',Id)
        self.output_text.insert(tk.END, f"==> Bravo AI : {text}\n")
        engine.say(text)
        engine.runAndWait()

    def openCam(self):
        vid = cv2.VideoCapture(0)
        while(True):
            ret, frame = vid.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
        vid.release()
        cv2.destroyAllWindows()

    def brain(self, query):
        # Your brain function implementation here
        pass

def main():
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()


main()