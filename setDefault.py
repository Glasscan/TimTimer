from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog


def setDefault():
    root = Tk()
    root.filename = tkFileDialog.askopenfilename(initialdir = "C:/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("wav files",".wav")))
    print (root.filename)

    default = open("DEFAULT.txt", 'w')
    default.write(root.filename)
    default.close()
    
