from tkinter import *
import wolframalpha
import os
import wikipedia
import tkinter.messagebox
import speech_recognition as sr
import time

while True:
    r=sr.Recognizer()

    with sr.Microphone() as Source:
        print("Speak Something")
        audio=r.listen(Source)
        try:
            text=r.recognize_google(audio)
            if text=="stop":
                break
            else:
                window=Tk()
                window.geometry("800x600")
                try:
                    app_id("KA57PT-5LQJER3L28")
                    client=wolframalpha.Client(app_id)
                    res = client.query(text)
                    answer=next(res.results).text

                    label1=Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font='roman,12 bold')
                    label1.pack()
                    window.after(5000,lambda:window.destroy())
                    mainloop()
                except:
                    answer=wikipedia.summary()
                    label1 = Label(window, justify=LEFT, compound=CENTER, padx=10, text=answer, font='roman,12 bold')
                    label1.pack()
                    window.after(500000, lambda: window.destroy())
                    mainloop()


        except:
            answer="sorry i dont understand what you say"
            print(answer)