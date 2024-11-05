from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import speech_recognition as sr


def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        sor_txt.delete(1.0, END)
        sor_txt.insert(END, text)
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
    except sr.RequestError:
        print("Could not connect to the speech recognition service.")


def translate():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x500")
root.configure(bg='light blue')


# Top Frame
Top_frame = Frame(root, bg="black", width=2300, height=155)
Top_frame.place(x=0, y=0)


Label_txt = Label(root, text="Text Translator", font=("Time New Roman", 40, "bold"))
Label_txt.place(x=270, y=40, height=60, width=870)


index = PhotoImage(file="C:\\text to speech\\images\\index.png")
Label(Top_frame, image=index, bg="white").place(x=18, y=5)


Frame = Frame(root).pack(side=BOTTOM)


Label_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"))
Label_txt.place(x=550, y=165, height=30, width=280)


sor_txt = Text(Frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=210, height=150, width=1340)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(Frame, value=list_text)
comb_sor.place(x=50, y=380, height=40, width=200)
comb_sor.set("English")


button_change = Button(Frame, text="Translate", relief=RAISED, command=translate)
button_change.place(x=500, y=380, height=40, width=350)


comb_dest = ttk.Combobox(Frame, value=list_text)
comb_dest.place(x=1100, y=380, height=40, width=200)
comb_dest.set("English")


dest_txt = Label(root, text="Dest Text", font=("Time New Roman", 20, "bold"))
dest_txt.place(x=600, y=430, height=40, width=170)


dest_txt = Text(Frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=480, height=150, width=1340)


button_listen = Button(Frame, text="Listen", relief=RAISED, command=recognize_speech)
button_listen.place(x=260, y=380, height=40, width=150)


root.mainloop()

