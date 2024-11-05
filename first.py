import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound

root=Tk()
root.title("TEXT TO SPEECH CONVERTER")
root.geometry("1000x500")
root.resizable(True,True)
root.configure(bg="light blue") 

engine = pyttsx3.init()
def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed == 'Fast'): 
            engine.setProperty('rate',250) 
            setvoice()
        elif(speed == 'Medium'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()              
#speaknow()


            
#Top Frame
Top_frame=Frame(root,bg="black",width=2300,height=173)
Top_frame.place(x=0,y=0)   


index=PhotoImage(file="C:\\text to speech\\images\\index.png")
Label(Top_frame,image=index,bg="white").place(x=18,y=5)



Label(Top_frame,text="TEXT TO SPEECH CONVERTER",font="arial 32  bold",fg="black").place(x=200,y=55)


###########


text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=60,y=250,width=600,height=380)


Label(root,text="Select Voice",font="arial 17 bold",fg="black").place(x=780,y=280)
Label(root,text="Select Speed",font="arial 17 bold",fg="black").place(x=1120,y=280)


gender_combobox=Combobox(root,values=['Male','Female',],font="arial 17",state='r',width=13)
gender_combobox.place(x=770,y=320) 
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Medium','Fast','Slow'],font="arial 17",state='r',width=13)
speed_combobox.place(x=1100,y=320) 
speed_combobox.set('Medium')


btn=Button(root,text="PLAY",command = speaknow, width=30,font="arial 17 bold")
btn.place(x=815,y=500)



root.mainloop()

