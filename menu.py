

from tkinter import *
import socket
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pickle
from datetime import datetime
import os
import threading
import struct

window = Tk()

window.title("Chat")
window.geometry("500x350")


background = Image.open("images/aea.png")
background = background.resize((550, 400), Image.ANTIALIAS)
background = ImageTk.PhotoImage(background)
#window.configure(background='sky blue')


def submit():
    window.destroy()
    from xdxd import FirstScreen
    #FirstScreen
def submit2():
    window.destroy()
    from chat_client_voz import FirstScreen
    #FirstScreen
def submit3():
    window.destroy()
    from chat_client_original import FirstScreen
    #FirstScreen


tk.Label(image=background).place(x=0, y=0)

my_button = Button(window,text="Chat-Señas",command=submit,width=20,height=3)
my_button.pack(pady=30)

my_button = Button(window,text="Chat-Voz",command=submit2,width=20,height=3)
my_button.pack(pady=20)

my_button = Button(window,text="Chat-Escritura",command=submit3,width=20,height=3)
my_button.pack(pady=20)

window.mainloop()