import tkinter as tk
from tkinter import Frame, Label, Scrollbar, Canvas
import json

# Load data
with open("sample.json", "r") as file:
    data = json.load(file)

# Initialize the root window
root = tk.Tk()
root.title("Slang Dictionary")
root.geometry("500x500")
root.config(bg="lightblue")

# Center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# Create a canvas and a scrollbar
canvas = Canvas(root, bg="lightblue")
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="lightblue")

# Configure the canvas
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add each word and definition to the frame as a label
for key, value in data.items():
    word_frame = Frame(scrollable_frame, bg="white", bd=2, relief="groove", padx=5, pady=5)
    word_frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    word_label = Label(word_frame, text=key, font=('Arial', 16, 'bold'), bg="white", anchor="w")
    word_label.pack(fill="x")
    
    meaning_label = Label(word_frame, text=value, font=('Arial', 12), bg="white", anchor="w", wraplength=450, justify='left')
    meaning_label.pack(fill="x")

# Run the application
root.mainloop()
