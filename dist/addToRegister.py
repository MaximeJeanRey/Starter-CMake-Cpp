import tkinter
from tkinter import messagebox

# Move and remove EasyPath.exe and EasyPath.ico to C:/Program Files/EasyPath
import shutil

#Get the language of the system
import locale
language = locale.getdefaultlocale()[0]

#Create the folder C:/Program Files/EasyPath
import os
os.mkdir("C:\Program Files\EasyPath")

# Move EasyPath.exe to C:/Program Files/EasyPath
if language == "fr_FR":
    shutil.move("EasyPath.exe", "C:\Programmes\EasyPath")
elif language == "en_US":
    shutil.copy("EasyPath.exe", "C:/Program Files/EasyPath/EasyPath.exe")
else :
    tkinter.messagebox.showerror("Error", "Your language is not supported yet")


# # Move EasyPath.exe to C:/Program Files/EasyPath
# shutil.copy("EasyPath.exe", "C:/Program Files/EasyPath/EasyPath.exe")
# shutil.copy("EasyPath.ico", "C:/Program Files/EasyPath/EasyPath.ico")

# Remove EasyPath.exe and EasyPath.ico from the dist folder
import os
os.remove("EasyPath.exe")
os.remove("EasyPath.ico")


# Add a key to the HKEY_CLASSES_ROOT\Directory\Background\shell registry key
# This will add a new menu item to the right click menu of the windows explorer

# Import the winreg module
import winreg

# Create a new key
# The key will be named "EasyPath"
newKey = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"Directory\Background\shell\EasyPath")

# Set the value of the new key
# The value will be "Add HERE to path"
winreg.SetValueEx(newKey, "", 0, winreg.REG_SZ, "Add to path")

# Create a new sub key
# The sub key will be named "command"
newSubKey = winreg.CreateKey(newKey, "command")

# Set the value of the sub key
# The value will be the path to the EasyPath.exe file
winreg.SetValueEx(newSubKey, "", 0, winreg.REG_SZ, r"C:\Users\mrey5\Documents\Programmation\EasyPath\dist\EasyPath.exe" "%V")

# Add an icon to the new menu item
# The icon will be the path to the EasyPath.ico file
winreg.SetValueEx(newKey, "Icon", 0, winreg.REG_SZ, r"C:\Users\mrey5\Documents\Programmation\EasyPath\dist\EasyPath.ico")

