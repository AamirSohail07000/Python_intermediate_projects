from tkinter import *
import pygame
from PIL import Image, ImageTk  # Import classes from Pillow to work with images
from tkinter import filedialog
import time
from mutagen.mp3 import MP3 # pip install mutagen and import MP3 to show length of song
import tkinter.ttk as ttk


music_p = Tk()
music_p.geometry("450x550")
music_p.config(bg="#ffffff")
music_p.title("A-Z Music Player")
music_p.resizable(False, False)

#Initialize pygame mixter
pygame.mixer.init()

# get song length time info
def play_time():
    # ge current song elapse time
    current_time = pygame.mixer.music.get_pos()/1000 #convert mili seconds to seconds


    # Convert to time format
    convert_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Get currently playing song
    
    # get song title from playlist
    song = list_box.get(ACTIVE)
    # Add directory file path and mp3 to the title
    song = f'C:/New folder Aamir/MCA/Music/{song}.mp3'

    # load song with Mutagen
    song_mut = MP3(song)
    # Get song Length
    global song_length 
    song_length = song_mut.info.length
    convert_time_length = time.strftime('%M:%S', time.gmtime(song_length))

    # Output time to status bar
    status_bar.config(text=f'Time Elapsed: {convert_time} of {convert_time_length}  ')
    # Update slider position value to current song position
    my_slider.config(value=int(current_time))
   

    # Update time each second i.e 1000 mili second
    status_bar.after(1000, play_time)

# Add song function
def add_song():
    song = filedialog.askopenfilename(initialdir="C:/New folder Aamir/MCA", title="Choose A Song", filetypes=(("Mp3 Files", "*.mp3"), ))
    
    #Strip out the directory info and .mp3 
    song = song.replace("C:/New folder Aamir/MCA/Music/", "")
    song = song.replace(".mp3", "")
   

    #Add song to listbox
    list_box.insert(END, song)

def add_multiple_songs():
    songs = filedialog.askopenfilenames(initialdir="C:/New folder Aamir/MCA", title="Choose Multiple Songs", filetypes=(("Mp3 Files", "*.mp3"), ))

    #Loop through song list to replace path and mp3 name
    for song in songs:
        song = song.replace("C:/New folder Aamir/MCA/Music/", "")
        song = song.replace(".mp3", "")
        #Add song to listbox
        list_box.insert(END, song)    

# Delete selected song from playlist
def delete_song():
    list_box.delete(ANCHOR)
    # Stop music if its playing
    pygame.mixer.music.stop()
# Delete all songs from playlist
def delete_all_songs():
    list_box.delete(0, END)
    # Stop music if its playing
    pygame.mixer.music.stop()          


# Play song
def play():
    song = list_box.get(ACTIVE)
    song = f'C:/New folder Aamir/MCA/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call the play_time function to get song length
    play_time()

    # Update Slider to position
    slider_position = int (song_length)
    my_slider.config(to=slider_position, value = 0)


# Stop playing current song and clear selection   
def stop():
    pygame.mixer.music.stop()
    list_box.select_clear(ACTIVE)

    # Clear status bar
    status_bar.config(text='')

# Play next song 
def next_song():
    # get the current song tuple number
    play_next = list_box.curselection()
    # Add one to the current song number
    play_next = play_next[0] + 1
    # get song title from playlist
    song = list_box.get(play_next)
    # Add directory file path and mp3 to the title
    song = f'C:/New folder Aamir/MCA/Music/{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # clear active bar in playlist
    list_box.selection_clear(0, END)
    # move active bar to next song which is playing now
    list_box.activate(play_next)
    #Set active bar to next song
    list_box.selection_set(play_next, last= None)    

# Play previous song in playlist
def prev_song():
    # get the current song tuple number
    play_next = list_box.curselection()
    # Add one to the current song number
    play_next = play_next[0] - 1
    # get song title from playlist
    song = list_box.get(play_next)
    # Add directory file path and mp3 to the title
    song = f'C:/New folder Aamir/MCA/Music/{song}.mp3'
    # Load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # clear active bar in playlist
    list_box.selection_clear(0, END)
    # move active bar to next song which is playing now
    list_box.activate(play_next)
    #Set active bar to next song
    list_box.selection_set(play_next, last= None)   


# Create pause variable
global paused
paused = False
# pause and unpause function
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

# Create slider function
def slide(x):
    # slider_label.config(text=my_slider.get())
    slider_label.config(text= f'{int(my_slider.get())} of {int(song_length)}')
    

#Create playlist
list_box = Listbox(music_p, bg="light blue", fg="black", width=60, selectbackground="gray", selectforeground="black")
list_box.pack(pady=20)


# Function to resize the image based on the specified width and height
def resize_image(image_path, width, height):
    image = Image.open(image_path)  # Open the image file from the given path
    # Resize the image to the width and height passed as arguments, and maintain the quality
    resized_image = image.resize((width, height), Image.LANCZOS)  
    # Convert the resized image to a format that Tkinter can use (PhotoImage)
    return ImageTk.PhotoImage(resized_image)

# Set the width and height for the button images (adjust these to control the size of buttons)
button_width = 50  # Width of the image in pixels
button_height = 50  # Height of the image in pixels

# Resize each button image to the specified size
back_button_img = resize_image("C:/New folder Aamir/MCA/button icons/back.png", button_width, button_height)
next_button_img = resize_image("C:/New folder Aamir/MCA/button icons/next.png", button_width, button_height)
pause_button_img = resize_image("C:/New folder Aamir/MCA/button icons/pause.png", button_width, button_height)
play_button_img = resize_image("C:/New folder Aamir/MCA/button icons/play.png", button_width, button_height)
stop_button_img = resize_image("C:/New folder Aamir/MCA/button icons/stop.png", button_width, button_height)

# Create a frame (container) to hold the control buttons
controls_frame = Frame(music_p, bg="#ffffff")  # 'music_p' is the main window or parent frame
controls_frame.pack()  # Pack the frame so it's visible on the window

# Create buttons for each control and assign the corresponding resized images
back_button = Button(controls_frame, image=back_button_img, borderwidth=0, bg="#ffffff", command= prev_song)  # 'borderwidth=0' removes button borders
next_button = Button(controls_frame, image=next_button_img, borderwidth=0, bg="#ffffff", command= next_song)
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0,bg="#ffffff", command= lambda: pause(paused))
play_button = Button(controls_frame, image=play_button_img, borderwidth=0, bg="#ffffff", command=play)
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0, bg="#ffffff", command=stop)

# Use grid layout to place the buttons in a row (one row, multiple columns)
back_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0,column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)  
stop_button.grid(row=0, column=3, padx=10)  
next_button.grid(row=0, column=4, padx=10)  

#Create Menu
my_menu = Menu(music_p)
music_p.config(menu=my_menu)

#Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One song to playlist", command=add_song)

# Add multiple songs to playlist
add_song_menu.add_command(label="Add Multiple songs to playlist", command= add_multiple_songs)

# Create Delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu = remove_song_menu)
remove_song_menu.add_command(label="Delete One Song from Playlist", command= delete_song)
remove_song_menu.add_command(label="Delete All Song from Playlist", command= delete_all_songs)

# Create status bar
status_bar = Label(music_p, text = '', bd=1, relief=GROOVE, anchor= E)
status_bar.pack(fill=X, side = BOTTOM, ipady = 2)

# Create Music Position slider
my_slider = ttk.Scale(music_p, from_=0, to = 100, orient = HORIZONTAL, value=0, command= slide, length= 360)
my_slider.pack(pady=35)

# Create temp slider lavel
slider_label = Label(music_p, text="0", bg="#ffffff")
slider_label.pack(pady=10)

music_p.mainloop()
