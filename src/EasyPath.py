# get the current path
import os
currentPath = os.getcwd()

# Add the current path to the system path
import sys
sys.path.append(os.getcwd())

# Print a pop up message
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Path",  currentPath + " added to system path")

