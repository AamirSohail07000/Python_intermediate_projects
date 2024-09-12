from tkinter import *
import pygame
from PIL import Image, ImageTk  # Import classes from Pillow to work with images
from tkinter import filedialog



music_p = Tk()
music_p.geometry("600x400")
music_p.config(bg="#333333")
music_p.title("A-Z Music Player")
music_p.resizable(False, False)

#Initialize pygame mixter
pygame.mixer.init()

#Add song function
def add_song():
    song = filedialog.askopenfilename(initialdir="C:/New folder Aamir/MCA", title="Choose A Song", filetypes=(("Mp3 Files", "*.mp3"), ))
    
    #Strip out the directory info and .mp3 
    song = song.replace("C:/New folder Aamir/MCA/Music/", "")
    song = song.replace(".mp3", "")
   

    #Add song to listbox
    list_box.insert(END, song)

def play():
    song = list_box.get(ACTIVE)
    song = f'C:/New folder Aamir/MCA/Music/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Stop playing current song and clear selection   
def stop():
    pygame.mixer.music.stop()
    list_box.select_clear(ACTIVE)

def pause():
    pygame.mixer.music.pause()

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
controls_frame = Frame(music_p, bg="#333333")  # 'music_p' is the main window or parent frame
controls_frame.pack()  # Pack the frame so it's visible on the window

# Create buttons for each control and assign the corresponding resized images
back_button = Button(controls_frame, image=back_button_img, borderwidth=0, bg="#333333")  # 'borderwidth=0' removes button borders
next_button = Button(controls_frame, image=next_button_img, borderwidth=0, bg="#333333")
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0,bg="#333333", command=pause)
play_button = Button(controls_frame, image=play_button_img, borderwidth=0, bg="#333333", command=play)
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0, bg="#333333", command=stop)

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


music_p.mainloop()
