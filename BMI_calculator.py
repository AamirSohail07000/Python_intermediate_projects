import tkinter as tk  # Import tkinter with an alias
from tkinter import * 

def bmi_category(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi <= 24.9:
        return "Normal Weight"
    elif 24.9 < bmi <= 29.9:
        return "Overweight"
    elif bmi >= 30:
        return "Obesity"

def calculate_bmi():
    try:
        weight = float(input_weight.get())
        height = float(input_height.get())
    except ValueError:
        # Handle the error if the input is not a valid number
        result_label.config(text="Please enter valid numbers for weight and height")
        return
    bmi = weight / ((height * 0.0254)** 2)  # Calculate BMI
    result_label.config(text=f"BMI : {bmi:.2f}\nBMI Category : {bmi_category(bmi)}")


bmi = tk.Tk()  # Create the main window using the tk.Tk() object
bmi.geometry("600x600")
bmi.config(bg="#D8BFD8")
bmi.title("BMI Calculator")
bmi.resizable(False, False)  # Disable window resizing (both horizontally and vertically)

# Create a header using tk.Label
head_label = tk.Label(bmi, text="Calculate BMI", fg="#8B4513", font=("Arial", 35, "bold"))
head_label.pack(side="top", fill=tk.X, pady=(40, 0))

# Create an input field for height and weight using tk.Entry
height_label = tk.Label(bmi, text="Enter Height (inc):", fg="#000000", font=("Arial", 15, "bold"))
height_label.place(x=110, y=120,height=35, width=180)

input_height = tk.StringVar()  # StringVar to store user input
height_entry = tk.Entry(bmi, textvariable=input_height, font=("Arial", 15, "bold"))  # Entry widget for weight input
height_entry.place(x=300, y=120, height=35, width=120)  # Position the Entry widget


weight_label = tk.Label(bmi, bg="#F5FFFA", text="Enter Weight (kg):", fg="#000000", font=("Arial", 15, "bold"))
weight_label.place(x=110, y=180,height=35, width=180)

input_weight = tk.StringVar()  # StringVar to store user input
weight_entry = tk.Entry(bmi, textvariable=input_weight, font=("Arial", 15))  # Entry widget for weight input
weight_entry.place(x=300, y=180,height=35, width=120)  # Position the Entry widget

result_label = tk.Label(bmi,text="", fg="#8B4513",bg="#D8BFD8", font=("Helvetica", 16, "bold"))
result_label.place(x=150, y=235)

# Button to submit and calculate BMI
Calculate_button = Button(bmi, text="Calculate", fg="white", bg="#039c08", font=("Arial", 15, "bold"), command=calculate_bmi)
Calculate_button.place(x=220, y=300, height=40, width=120) 

bmi.mainloop()  # Start the Tkinter event loop
