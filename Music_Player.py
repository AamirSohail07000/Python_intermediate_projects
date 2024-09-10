import tkinter as tk
from tkinter import filedialog
import os
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Global variables to store the song list and current index
music_files = []
current_song_index = 0
is_playing = False

# Function to load and play a song
def load_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    update_song_label(song)
    global is_playing
    is_playing = True
    play_pause_button.config(text="Pause")

# Function to select folder or music file and load music files
def select_folder():
    global music_files, current_song_index
    folder_path = filedialog.askdirectory()
    if folder_path:
        all_files = os.listdir(folder_path)
        music_files = [os.path.join(folder_path, file) for file in all_files if file.endswith(('.mp3', '.wav'))]
        if music_files:
            current_song_index = 0
            load_music(music_files[current_song_index])
        else:
            result_label.config(text="No music files found in the selected folder.")
    else:
        file_path = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav")])
        if file_path:
            music_files = [file_path]
            current_song_index = 0
            load_music(music_files[current_song_index])
        else:
            result_label.config(text="No music file selected.")

# Function to play the next song when the current one ends
def play_next_song():
    global current_song_index
    if music_files:
        current_song_index += 1
        if current_song_index < len(music_files):
            load_music(music_files[current_song_index])
        else:
            result_label.config(text="End of playlist.")
            stop_music()

# Function to play the previous song
def play_prev_song():
    global current_song_index
    if music_files:
        current_song_index -= 1
        if current_song_index >= 0:
            load_music(music_files[current_song_index])
        else:
            result_label.config(text="You are at the beginning of the playlist.")

# Function to update the label with the current song
def update_song_label(song):
    song_name = os.path.basename(song)
    result_label.config(text=f"🎶 Now playing: {song_name} 🎶")

# Function to toggle play/pause
def toggle_play_pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
        play_pause_button.config(text="Play")
        is_playing = False
    else:
        pygame.mixer.music.unpause()
        play_pause_button.config(text="Pause")
        is_playing = True

# Function to stop the current song
def stop_music():
    pygame.mixer.music.stop()
    result_label.config(text="Music stopped.")
    play_pause_button.config(text="Play")
    global is_playing
    is_playing = False

# Create the main window
music_p = tk.Tk()
music_p.geometry("600x400")
music_p.config(bg="#333333")
music_p.title("A-Z Music Player")
music_p.resizable(False, False)

# Header label
heading_label = tk.Label(music_p, text="A-Z Music Player", bg="#1c1c1c", fg="#FFD700", font=("Arial", 30, "bold"))
heading_label.place(relx=0.0, rely=0.0, relwidth=1.0)

# Label to display current song
result_label = tk.Label(music_p, text="", font=("Arial", 16), fg="#FFD700", bg="#333333")
result_label.place(relx=0.0, rely=0.3, relwidth=1.0)

# Define a style for buttons
button_style = {"bg": "#556B2F", "fg": "#ffffff", "font": ("Arial", 15, "bold"), "bd": 5, "relief": "raised"}

# Create buttons and position them in the center
play_pause_button = tk.Button(music_p, text="Play", command=toggle_play_pause, **button_style)
play_pause_button.place(relx=0.5, rely=0.6, anchor="center", width=100, height=50)

next_button = tk.Button(music_p, text="Next", command=play_next_song, **button_style)
next_button.place(relx=0.65, rely=0.6, anchor="center", width=100, height=50)

prev_button = tk.Button(music_p, text="Prev", command=play_prev_song, **button_style)
prev_button.place(relx=0.35, rely=0.6, anchor="center", width=100, height=50)

select_folder_button = tk.Button(music_p, text="Select Folder", command=select_folder, **button_style)
select_folder_button.place(relx=0.5, rely=0.75, anchor="center", width=200, height=50)

# Function to check for the next song when the current one ends
def check_music_event():
    if not pygame.mixer.music.get_busy() and music_files and is_playing:
        play_next_song()
    music_p.after(1000, check_music_event)

# Start the music event checker
check_music_event()

music_p.mainloop()
