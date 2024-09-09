from tkinter import *
import tkinter as tk
import os
import pygame

music_p = tk.Tk()
music_p.geometry("550x750")
music_p.config(bg="#87CEEB")
music_p.title("Music Player")
music_p.resizable(False, True)


heading_label = Label(text="A-Z Music Player", bg="#696969",fg="#191970",font=("Arial", 25, "bold"))
heading_label.place(relx=0.0, rely = 0.0, relwidth= 1.0)

#Buttons for Play , Pause, Stop and Select Folder
play_button = Button(text="Play", bg="#556B2F",fg="#ffffff",font=("Arial", 25, "bold"))
play_button.place(x= 30, y=80, width=200)

pause_button = Button(text="Pause", bg="#556B2F",fg="#ffffff",font=("Arial", 25, "bold"))
pause_button.place(x= 280, y=80, width=250)

stop_button = Button(text="Stop", bg="#556B2F",fg="#ffffff",font=("Arial", 25, "bold"))
stop_button.place(x= 30, y=210, width=200)

select_folder_button = Button(text="Select Folder", bg="#556B2F",fg="#ffffff",font=("Arial", 25, "bold"))
select_folder_button.place(x= 280, y=210, width=250)





music_p.mainloop()