import tkinter as tk  # Import tkinter with an alias
from tkinter import * 

def calculate_bmi():
  try:
    weight = float(input_weight.get())
    height = float(input_height.get())
  except ValueError:
    # Handle the error if the input is not a valid number
    result_label.config(text="Please enter valid numbers for weight and height")
    return
  bmi = weight / ((height * 0.0254)** 2)  # Calculate BMI
  result_label.config(text=f"Your BMI is {bmi:.2f}") #result in Floating point number upto 2 decimals

bmi = tk.Tk()  # Create the main window using the tk.Tk() object
bmi.geometry("600x600")
bmi.config(bg="#D8BFD8")
bmi.title("BMI Calculator")
bmi.resizable(False, False)  # Disable window resizing (both horizontally and vertically)

# Create a header using tk.Label
head_label = tk.Label(bmi, text="Calculate BMI", fg="#8B4513", font=("Arial", 35, "bold"))
head_label.pack(side="top", fill=tk.X, pady=(40, 0))

# Create an input field for height and weight using tk.Entry
height_label = tk.Label(bmi, text="Enter Height(inc):", fg="#8B008B", font=("Arial", 15, "bold"))
height_label.place(x=110, y=120,height=35, width=180)

input_height = tk.StringVar()  # StringVar to store user input
height_entry = tk.Entry(bmi, textvariable=input_height, font=("Arial", 15, "bold"))  # Entry widget for weight input
height_entry.place(x=300, y=120, height=35, width=120)  # Position the Entry widget


weight_label = tk.Label(bmi, bg="#F5FFFA", text="Enter Weight(kg):", fg="#8B008B", font=("Arial", 15, "bold"))
weight_label.place(x=110, y=180,height=35, width=180)

input_weight = tk.StringVar()  # StringVar to store user input
weight_entry = tk.Entry(bmi, textvariable=input_weight, font=("Arial", 15))  # Entry widget for weight input
weight_entry.place(x=300, y=180,height=35, width=120)  # Position the Entry widget

result_label = tk.Label(bmi,text="", fg="#8B4513",bg="#D8BFD8", font=("Arial", 18, "bold"))
result_label.place(x=130, y=235,height=45, width=300)



# Button to submit and calculate BMI
Calculate_button = Button(bmi, text="Calculate", fg="white", bg="#039c08", font=("Arial", 15, "bold"), command=calculate_bmi)
Calculate_button.place(x=220, y=300, height=40, width=120) 







bmi.mainloop()  # Start the Tkinter event loop
