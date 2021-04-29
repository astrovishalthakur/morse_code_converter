# TODO 0. Create a dictionary to store values of morse code for each alphabet.
# TODO 1. Define a function to take string argument and convert it to morse code.
# TODO 2. Define a function to take morse code and convert it to string.


print("Please use alphabets, numbers, comma, slash, dash, dot, parenthesis and question mark only.")

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

key_list = list(MORSE_CODE_DICT.keys())
val_list = list(MORSE_CODE_DICT.values())

def code(text):
    morse = ""
    text = text.upper()
    for n in text:
        if n == " ":
            morse = morse + "|   "
        else:
            m = MORSE_CODE_DICT[n]
            morse = morse + f"{m}   "
    return morse


def decode(morse):
    text = ""
    lis1 = morse.split("|")
    for n in lis1:
        n = n.strip()
        lis2 = n.split("   ")
        for m in lis2:
            ind = val_list.index(m)
            w = key_list[ind]
            text = text + w
        text = text + " "
    return text


string = input("enter text.")
morse = code(string)
dec = decode(morse)

print(morse)
print(dec)
