import os
from pygame import mixer
from tkinter import *
import os


root = Tk()
root.title('Music player')

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    len_currentsong = int(mixer.Sound("D:\Directory\Documents\La_Plateforme\Python\PlayerMusic\{}".format(currentsong)).get_length()*1000)
    mixer.music.load(currentsong)
    mixer.music.play()

def pausesong():
    mixer.music.pause()
    print(mixer.music.get_pos())

def stopsong():
    mixer.music.stop()

def resumesong():
    mixer.music.unpause()

mixer.init()
mixer.Channel
playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=40)
playlist.grid(columnspan=5)

songs = os.listdir()
for s in songs:
    if '.mp3' in s:
        playlist.insert(END, s)

playbtn = Button(root, text="play", command=playsong)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pausesong)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text="Stop", command=stopsong)
stopbtn.grid(row=1, column=2)

Resumebtn = Button(root, text="Resume", command=resumesong)
Resumebtn.grid(row=1, column=3)

mainloop() 