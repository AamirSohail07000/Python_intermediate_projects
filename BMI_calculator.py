import tkinter as tk  # Import tkinter with an alias

bmi = tk.Tk()  # Create the main window using the tk.Tk() object
bmi.geometry("600x600")
bmi.config(bg="#D8BFD8")
bmi.title("BMI Calculator")
bmi.resizable(False, False)  # Disable window resizing (both horizontally and vertically)

# Create a header using tk.Label
head_label = tk.Label(bmi, bg="#F5FFFA", text="Calculate BMI", fg="#8B4513", font=("Arial", 35, "bold"))
head_label.pack(side="top", fill=tk.X, pady=(40, 0))

# Create an input field for weight using tk.Entry
input_weight = tk.StringVar()  # StringVar to store user input
weight_entry = tk.Entry(bmi, textvariable=input_weight, font=("Arial", 14))  # Entry widget for weight input
weight_entry.place(x=240, y=120, width=120)  # Position the Entry widget

bmi.mainloop()  # Start the Tkinter event loop