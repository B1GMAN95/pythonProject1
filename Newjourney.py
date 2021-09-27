from tkinter import *
from tkinter import filedialog, Text
import os

import tkinter as tk

root = tk.Tk()
root.geometry("700x700")


frame = tk.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)

text = Label(root, text="DuqPro")
text.pack()
canvas = tk.Canvas(root, height=50, width=10000, bg="#FFFF00")
canvas.pack()


Lagswitch = tk.Button(root, text="Dupe Guns", width=15, padx=10, pady=5, fg="purple", bg="#00FFFF")
Lagswitch.pack()


root.mainloop()


