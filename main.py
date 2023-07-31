from customtkinter import *
import pyperclip
import secrets
import string

root = CTk() #Tk
root.geometry("700x350") # 250, now 350
root.title("Password Generator 3.0")

## FUNCTIONS ##
roundedVal = 12
global addLetters
addLetters = "on"
global addNumbers
addNumbers = "on"
global addChars
addChars = "on"
def generatePassword():
    letters = string.ascii_letters 
    digits = string.digits
    special_chars = string.punctuation
    #alphabet = letters + digits + special_chars

    ### Toggles ###
    alphabet = ""
    if addLetters == "on":
        alphabet = alphabet + letters
    if addNumbers == "on":
        alphabet = alphabet + digits
    if addChars == "on":
        alphabet = alphabet + special_chars

    ### Errors ###
    if (addLetters == "off") and (addNumbers == "off") and (addChars == "off"):
        passwordText.configure(text="Can't create password with no input.", fg_color="red")
    else:
        # Everything below will be indented
        pwd_length = roundedVal

        global pwd

        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        
        passwordText.configure(text=pwd, fg_color="#434756")


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

def checkbox_event1():
    global addLetters
    addLetters = check_var1.get()

def checkbox_event2():
    global addNumbers
    addNumbers = check_var2.get()

def checkbox_event3():
    global addChars
    addChars = check_var3.get()


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

# Checkboxes #
blankSpace2 = CTkLabel(root, text="")
blankSpace2.pack()


check_var1 = StringVar(value="on")
letterBox = CTkCheckBox(root, text="Add letters", command=checkbox_event1, variable=check_var1, onvalue="on", offvalue="off")
letterBox.pack(pady=5)

check_var2 = StringVar(value="on")
numberBox = CTkCheckBox(root, text="Add numbers", command=checkbox_event2, variable=check_var2, onvalue="on", offvalue="off")
numberBox.pack(pady=5)

check_var3 = StringVar(value="on")
charBox = CTkCheckBox(root, text="Add characters", command=checkbox_event3, variable=check_var3, onvalue="on", offvalue="off")
charBox.pack(pady=5)


## Run GUI ##
root.mainloop()
