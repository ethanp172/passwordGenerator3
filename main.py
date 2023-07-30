from customtkinter import *
import pyperclip
import secrets
import string

root = CTk() #Tk
root.geometry("700x250")
root.title("Password Generator 3.0")

## FUNCTIONS ##
roundedVal = 12
def generatePassword():
    letters = string.ascii_letters 
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    pwd_length = roundedVal

    global pwd

    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    
    passwordText.configure(text=pwd)

def lenSliderEvent(value):
    global roundedVal
    roundedVal = int(value)
    roundedStr = str(roundedVal)
    sayText = "Length: " + roundedStr
    sliderStats.configure(text=sayText)
    return roundedVal

def copyPaste():
    toCopy = pwd
    pyperclip.copy(pwd)

## CODE ##
mainTitle = CTkLabel(root, text="Password Generator 3.0", fg_color="transparent", font=('Roboto', 20))
mainTitle.pack(pady=2.5)

passwordText = CTkLabel(root, text="Password", font=('Courier New', 25), fg_color="#434756", corner_radius=8)
passwordText.pack(pady=5)

# Buttons #

passwordGenerate = CTkButton(root, text="Generate", command=generatePassword)
passwordCopy = CTkButton(root, text="Copy", command=copyPaste)

passwordGenerate.pack(pady=5)
passwordCopy.pack()

# Slider #

blankSpace = CTkLabel(root, text="")
blankSpace.pack()

sliderStats = CTkLabel(root, text="Length: 12")
sliderStats.pack()

lenSlider = CTkSlider(root, from_=1, to=45, number_of_steps=45, command=lenSliderEvent)
lenSlider.set(12)
lenSlider.pack()


root.mainloop()
