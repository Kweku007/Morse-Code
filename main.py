## Text to Morse Code Converter

db = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",		
    "f": "..-.",
    "g": "--.",	
    "h": "....",	
    "i": "..",	
    "j": ".---",	
    "k": "-.-",	
    "l": ".-..",	
    "m": "--",
    "n": "-.",
    "o": "---",	
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "=": "-...-",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    " ": "/",
}

stop = ["no", "NO", "n", "N"]

complete = False

print("Welcome to the Morse Code Converter Program!!!")
print("----------------------------------------------\n")

while not complete:
    user_text = input("\nWhat text would you like to be converted to Morse Code today? ")
    converted_text = ""

    for symbol in user_text:
        try:
            converted_symbol = db[symbol.lower()]
            converted_text += converted_symbol
            converted_text += " "
            correct_symbol = True
        except KeyError:
            print("The symbol {} is not in our Morse code dictionary, please try again".format(symbol))
            correct_symbol = False
            break

    if correct_symbol:
        print("\nThank you for the text the program completed with the following:")
        print(converted_text)
        user_continue = input("\nWould you like to continue? (Y/N) ")
        if user_continue in stop:
            complete = True

print("\nMorse Code Program Completed!!!")
print("---------------------------------")