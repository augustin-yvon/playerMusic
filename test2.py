import os
from pygame import mixer
from tkinter import *
from tkinter.ttk import Progressbar

root = Tk()
root.title('Music player')

# Fonction pour ajouter un fichier à la playlist
def add_to_playlist():
    song_file = filedialog.askopenfilename(initialdir=".", title="Select a song", filetypes=(("MP3 files", "*.mp3"),))
    if song_file != "":
        playlist.insert(END, os.path.basename(song_file))
        songs.append(song_file)

# Fonction pour lire une chanson à partir de la playlist
def play_song():
    currentsong = playlist.get(ACTIVE)
    len_currentsong = int(mixer.Sound(currentsong).get_length() * 1000)
    mixer.music.load(currentsong)
    mixer.music.play()
    progressbar['maximum'] = len_currentsong
    update_progressbar()

# Fonction pour mettre en pause la chanson en cours de lecture
def pause_song():
    mixer.music.pause()

# Fonction pour arrêter la chanson en cours de lecture
def stop_song():
    mixer.music.stop()
    progressbar['value'] = 0

# Fonction pour reprendre la lecture de la chanson en pause
def resume_song():
    mixer.music.unpause()
    update_progressbar()

# Fonction pour mettre à jour la barre de progression
def update_progressbar():
    current_pos = mixer.music.get_pos()
    if current_pos >= 0:
        progressbar['value'] = current_pos
        root.after(1000, update_progressbar)

# Initialisation de Pygame mixer
mixer.init()

# Ajout de chansons à la playlist
songs = []
for file in os.listdir("D:\Directory\Documents\La_Plateforme\Python\PlayerMusic"):
    if file.endswith('.mp3'):
        songs.append("D:\Directory\Documents\La_Plateforme\Python\PlayerMusic\{}".format(file))
for s in songs:
    playlist.insert(END, os.path.basename(s))

# Création de la barre de menu
menubar = Menu(root)
root.config(menu=menubar)

# Ajout du menu "File" à la barre de menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add to playlist", command=add_to_playlist)
file_menu.add_command(label="Exit", command=root.quit)

# Création de la playlist
playlist_frame = Frame(root)
playlist_frame.pack(side=LEFT, padx=10)
scrollbar = Scrollbar(playlist_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
playlist = Listbox(playlist_frame, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), width=40, yscrollcommand=scrollbar.set)
playlist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=playlist.yview)

# Création des boutons pour contrôler la lecture de la musique
controls_frame = Frame(root)
controls_frame.pack(side=LEFT, padx=10)
play_icon = PhotoImage(file="play.png")
playbtn = Button(controls_frame, image=play_icon, command=play_song, padx=10, pady=10)
playbtn.grid(row=0, column=0, padx=5, pady=5)
pause_icon = PhotoImage(file="pause.png")
pausebtn = Button(controls_frame, image=pause_icon, command=pause_song, padx=10, pady=10)
