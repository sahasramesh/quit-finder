import os
import tkinter as tk
from tkinter import *

window = Tk()
window.geometry('200x200')
window.title("quit finder")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.resizable(width=False, height=False)
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

def quit():
    os.system("defaults write com.apple.finder QuitMenuItem -bool true")
    os.system("""osascript -e 'quit app "Finder"'""")

    lbl.configure(text="was it worth it?")
    btn.config(state='disabled')

fr = Frame(window)
fr.grid(column=0, row=0)

lbl = Label(fr, text="let go of your fear.", font=("Times New Roman", 14))
lbl.grid(column=0, row=0)

btn = Button(fr, text="do it.", command=quit, font=("Times New Roman", 14))
btn.grid(column=0, row=1)

window.mainloop()
