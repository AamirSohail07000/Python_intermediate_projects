from tkinter import *
import pygame
from PIL import Image, ImageTk  # Import classes from Pillow to work with images
from tkinter import filedialog
import time
from mutagen.mp3 import MP3 # pip install mutagen and import MP3 to show length of song
import tkinter.ttk as ttk


music_p = Tk()
music_p.geometry("550x450")
music_p.config(bg="#fffcfc")
music_p.title("A-Z Music Player")
music_p.resizable(False, False)



#Initialize pygame mixter
pygame.mixer.init()

# get song length time info
def play_time():
    # Check for unwanted looping
    if stopped:
        return 
     # ge current song elapse time
    current_time = pygame.mixer.music.get_pos()/1000 #convert mili seconds to seconds
    # Throw up temp label to get data
    # slider_label.config(text=f'Slider:  {int(my_slider.get())} and Song Pos: {int(current_time)}')
    # # Convert to time format
    convert_time = time.strftime('%M:%S', time.gmtime(current_time))
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


    # Increase current_time by 1 sec
    current_time += 1
    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {convert_time_length}')
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        # Slider hasn't been moved
         # Update Slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value = int(current_time))
    else :
        # Slider has been moved
        # Update Slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value = int(my_slider.get()))
        # Convert to time format
        convert_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
        
        # Output time to status bar
        status_bar.config(text=f'Time Elapsed: {convert_time} of {convert_time_length}')
        # move this by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
    


    # Update slider position value to current song position
    # my_slider.config(value=int(current_time))
    
   
    # Update time each second i.e 1000 mili second
    status_bar.after(1000, play_time)

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
    stop()
    list_box.delete(ANCHOR)
    # Stop music if its playing
    pygame.mixer.music.stop()
# Delete all songs from playlist
def delete_all_songs():
    stop()
    list_box.delete(0, END)
    # Stop music if its playing
    pygame.mixer.music.stop()          


# Play song
def play():
    global paused
    paused = False
    # Reset slider and status bar
    status_bar.config(text="")
    my_slider.config(value=0)
    # If no song is currently selected, select the first one
    if not list_box.curselection():
        list_box.selection_set(0)  # Select the first song
        list_box.activate(0)  # Activate the first song
        
    song = list_box.get(ACTIVE)
    song = f'C:/New folder Aamir/MCA/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call the play_time function to get song length
    play_time()

    # Update Slider to position
    # slider_position = int (song_length)
    # my_slider.config(to=slider_position, value = 0)

# Play next song 
def next_song():
    
    # Reset slider and status bar
    status_bar.config(text="")
    my_slider.config(value=0)
    
    # get the current song tuple number
    play_next = list_box.curselection()
    # Add one to the current song number
    if play_next:
        play_next = play_next[0] + 1

        # Check if the current song is the last one in the playlist
        if play_next >= list_box.size():
            # If it's the last song, either stop or loop back to the first song
            play_next = 0  # Wrap back to the first song
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
        list_box.selection_set(play_next, last=None)    

# Play previous song in playlist
def prev_song():

    # Reset slider and status bar
    status_bar.config(text="")
    my_slider.config(value=0)
    
    # get the current song tuple number
    play_next = list_box.curselection()
    # Add one to the current song number
    if play_next:
        play_next = play_next[0] - 1

        if play_next < 0:
            play_next = list_box.size() - 1 # Wrap to the last song
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

global stopped
stopped = False
# Stop playing current song and clear selection   
def stop():
    # Reset slider and status bar
    status_bar.config(text="")
    my_slider.config(value=0)
    # Stop song from playing
    pygame.mixer.music.stop()

    # Clear active selection in the listbox
    list_box.select_clear(0, END)

    # Clear status bar
    status_bar.config(text='')
    # set Stopped variable to true
    global stopped
    stopped = True

# Create slider function
def slide(x):
    # slider_label.config(text=my_slider.get())
    # slider_label.config(text= f'{int(my_slider.get())} of {int(song_length)}')
    song = list_box.get(ACTIVE)
    song = f'C:/New folder Aamir/MCA/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start= int(my_slider.get()))

# Create Volume Function
def volume(X):
    pass




# Create master frame
master_frame = Frame(music_p)
master_frame.pack(pady=20)
master_frame.config(bg="#fffcfc")

#Create playlist
list_box = Listbox(master_frame, bg="light blue", fg="black", width=60, selectbackground="gray", selectforeground="black")
list_box.grid(row=0, column=0)


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
controls_frame = Frame(master_frame, bg="#fffcfc")  # 'music_p' is the main window or parent frame
controls_frame.grid(row=1, column=0, pady=25)  # Pack the frame so it's visible on the window

# Create volume Label frame 
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx= 20)

# Create buttons for each control and assign the corresponding resized images
back_button = Button(controls_frame, image=back_button_img, borderwidth=0, bg="#fffcfc", command= prev_song)  # 'borderwidth=0' removes button borders
next_button = Button(controls_frame, image=next_button_img, borderwidth=0, bg="#fffcfc", command= next_song)
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0,bg="#fffcfc", command= lambda: pause(paused))
play_button = Button(controls_frame, image=play_button_img, borderwidth=0, bg="#fffcfc", command=play)
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0, bg="#fffcfc", command=stop)

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
# create a new style to fix background color issue of slider
style = ttk.Style()
# Configure the background of the 'TScale' (for ttk.Scale)
style.configure("TScale", bg="#fffcfc")  # Replace "lightblue" with your desired color

# Create Music Position slider
my_slider = ttk.Scale(master_frame, from_=0, to = 100, orient = HORIZONTAL, value=0, command= slide, length= 360)
my_slider.grid(row=2, column=0,pady=15)

# Create Volume slider
volume_slider = ttk.Scale(volume_frame, from_=0, to = 1, orient = VERTICAL, value=1, command= volume, length= 125)
volume_slider.pack(pady=10)

# Create temp slider lavel
# slider_label = Label(music_p, text="0", bg="#fffcfc")
# slider_label.pack(pady=10)

music_p.mainloop()
