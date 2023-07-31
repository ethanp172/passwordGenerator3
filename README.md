# Password Generator V3
A simple password generator written in Python, using [Custom Tkinter](https://github.com/TomSchimansky/CustomTkinter). Every new language I learn, my first small project is a password generator.

![image](https://github.com/ethanp172/passwordGenerator3/assets/140129580/47e9b680-faf6-40ab-af82-c27709c6c430)

## How it works
You can edit a few settings, and then click `generate`. Then you have a securly generated password, that you can directly copy to your clipboard.  
Example: `ET&1^$c"c90w`

## Settings
**Length**
- How long your password will be
- By defualt, the value will be 12
- Min: 1, Max: 45  

**Letters**
- Adds letters into password
- Example: `sJbkNxbVbaCt`  

**Numbers**
- Adds numbers into passwor
- Example: `812045802389`  

**Symbols**
- Adds special symbols into password
- Example: `@(\=^&=;;>?]`  

## Packages Used
**Custom Tkinter:** Used for the GUI  
**Pyperclip:** Used to copy the password directly to clipboard  
**Secrets:** Used to generate the password  
