import tkinter as tk
from tkinter import Listbox
import json

with open("sample.json", "r") as file:
    data =json.load(file)

root = tk.Tk()

root.title("Slang Dictionary")

root.geometry("500x500")

listbox = Listbox(root, font=('Arial'))
listbox.pack(fill=tk.BOTH, expand=True)

for key, value in data.items():
    listbox.insert(tk.END,f"{key}:{value}")


root.mainloop()














#Label/Text like in HTML
#label = tk.Label(root, text= newlySorted, font=('Arial', 18))

#placement of text 
#label.pack(padx=20, pady=20)

#Textbox already text wrap
#textbox = tk.Text(root, height=3, font=('Arial', 15))
#textbox.pack()

