import tkinter as tk
from tkinter import *
import PyPDF2
import pyttsx3
from tkinter import filedialog
import tkinter.font as fnt
from PIL import Image, ImageTk

'''
engine = pyttsx3.init()  # object creation
# Rate
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 140)

# volume
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', volume+0.5)
print(engine.getProperty('volume'))

# Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)

engine.say("Hello abraham, My current speaking rate is " + str(
    rate) + " and the volume of my current voice is " + str(volume))
engine.runAndWait()
engine.stop()
'''


# function to browse a file
def browse():
    global pdfReader
    file = filedialog.askopenfilename(title="Select a PDF")
    pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))
    pathlabel.config(text=file)  # configuring the pathlabel Label


# Function to convert into Audio File
def save():
    global speaker
    speaker = pyttsx3.init()
    volume = speaker.getProperty('volume')
    speaker.setProperty('rate', 140)
    speaker.setProperty('volume', volume + 0.5)
    voices = speaker.getProperty('voices')
    if m.get() == 0:
        speaker.setProperty('voice', voices[0].id)
    else:
        speaker.setProperty('voice', voices[1].id)

    for page_num in range(pdfReader.numPages):
        text = pdfReader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()
    speaker.save_to_file(text, 'audio.mp3')
    speaker.runAndWait()
    Label(root, text="The Audio File is Saved Successfully!!").pack()


# Create GUI window
root = Tk()
root.geometry('950x800')
root.title("My Audio Book")
image_photo = PhotoImage(file="img.png")
Label(root, image=image_photo).pack()
pathlabel = Label(root)
pathlabel.pack()

m = tk.IntVar()
m.set(0)  # initialize the choice, i.e. male

Button(root, text="Browse a PDF File", font=fnt.Font(size=10), padx=10, pady=10, command=browse).pack()
Radiobutton(root, text="Male Voice", font=fnt.Font(size=10), padx=5, pady=5, variable=m, value=0).pack()
Radiobutton(root, text="Female Voice", font=fnt.Font(size=10), padx=5, pady=5, variable=m, value=1).pack()
Button(root, text="Create and Save the Audio File", font=fnt.Font(size=10), padx=10, pady=10, command=save).pack()

root.mainloop()
