#TEXT TO MORSE CODE CONVERTER
import os
from ascii import title

def clean_terminal():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

def setup():
    clean_terminal()
    print(title)

def restart_script_or_not():
    restart = input("Restart Script? [Y/N] \n").upper()
    if restart == "Y":
        return True
    else:
        return False

morse_dict = {
    # Letters
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

script_is_on = True

while script_is_on:
    setup()
    morse_code = []
    error_cat = False 

    string_input = input("Write a text to convert into morse code: ").upper()

    for char in string_input:
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        elif char == " ":
            morse_code.append("  ")
        else:
            error_cat = True
            
    if not error_cat:
        print(f"There is your morse code: {' '.join(morse_code)} ")
    else:
        print("Something went wrong! Please check that your text does not contain symbols.")
            
    script_is_on = restart_script_or_not()