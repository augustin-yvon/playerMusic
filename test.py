import os
from pygame import mixer
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Music player')

def playsong():
    currentsong = playlist.get(ACTIVE)
    len_currentsong = int(mixer.Sound("D:\Directory\Documents\La_Plateforme\Python\PlayerMusic\{}".format(currentsong)).get_length()*1000)
    mixer.music.load(currentsong)
    mixer.music.play()
    progressbar['maximum'] = len_currentsong
    update_progressbar()

def pausesong():
    mixer.music.pause()

def stopsong():
    mixer.music.stop()
    progressbar['value'] = 0

def resumesong():
    mixer.music.unpause()
    update_progressbar()

def update_progressbar():
    current_pos = mixer.music.get_pos()
    if current_pos >= 0:
        progressbar['value'] = current_pos
        root.after(1000, update_progressbar)

mixer.init()
playlist = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=40)
playlist.grid(columnspan=5)

songs = os.listdir("D:\Directory\Documents\La_Plateforme\Python\PlayerMusic")
for s in songs:
    if s.endswith('.mp3'):
        playlist.insert(END, s)


playbtn = Button(root, text='Play', command=playsong)
playbtn.grid(row=1, column=0)

pause_icon = PhotoImage(file='pause.png')
pausebtn = Button(root, image=pause_icon, command=pausesong)
pausebtn.grid(row=1, column=2)

stop_icon = PhotoImage(file='stop.png')
stopbtn = Button(root, image=stop_icon, command=stopsong)
stopbtn.grid(row=1, column=3)

play_icon = PhotoImage(file='play.png')
resumebtn = Button(root, image=play_icon, command=resumesong)
resumebtn.grid(row=1, column=1)

progressbar = Progressbar(root, orient='horizontal', length=600, mode='determinate')
progressbar.grid(row=2, column=0, columnspan=4)

mainloop()