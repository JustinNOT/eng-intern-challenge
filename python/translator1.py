import sys

# Braille alphabet to English mappings
BRAILLE_DICT = {
    # Lowercase letters
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "......": " ",

    # Capital letters (with .....O in front)
    ".....OO.....": "A", ".....OO.O...": "B", ".....OOO....": "C", ".....OOO.O..": "D", ".....O..O..": "E", ".....OOOO...": "F", ".....OOOOO..": "G",
    ".....O.OO..": "H", ".....O.OO...": "I", ".....O.OOO..": "J", ".....O...O.": "K", ".....O.O.O.": "L", ".....OO..O.": "M", ".....OO.OO.": "N",
    ".....O..OO.": "O", ".....OOO.O.": "P", ".....OOOOO.": "Q", ".....O.OOO.": "R", ".....O.OO.O.": "S", ".....O.OOOO.": "T", ".....O...OO": "U",
    ".....O.O.OO": "V", ".....O.OOO.O": "W", ".....OO..OO": "X", ".....OO.OOO": "Y", ".....O..OOO": "Z"
}

NUMBER_DICT = {
    # Original numbers
    ".O.OOOO.....": "1", ".O.OOOO.O...": "2", ".O.OOOOO....": "3", ".O.OOOOO.O..": "4", ".O.OOOO..O...": "5",
    ".O.OOOOOO...": "6", ".O.OOOOOOO..": "7", ".O.OOOO.OO...": "8", ".O.OOO.OO...": "9", ".O.OOO.OOO..": "0",

    # Decimal prefixed numbers (with .O...O in front)
    ".O...O.O.OOOO.....": ".1", ".O...O.O.OOOO.O...": ".2", ".O...O.O.OOOOO....": ".3", ".O...O.O.OOOOO.O..": ".4", ".O...O.O.OOOO..O...": ".5",
    ".O...O.O.OOOOOO...": ".6", ".O...O.O.OOOOOOO..": ".7", ".O...O.O.OOOO.OO...": ".8", ".O...O.O.OOO.OO...": ".9", ".O...O.O.OOO.OOO..": ".0"
}

CHAR_DICT = {
    "..OO.O": ".",  
    "..O...": ",",  
    "..O.OO": "?",  
    "..OOO.": "!",  
    "..OO..": ":",  
    "..O.O.": ";", 
    "....OO": "-",  
    ".O..O.": "/", 
    ".OO..O": "<",  
    "O..OO.": ">",
    "O.O..O": "(",  
    ".O.OO.": ")",  
    "......": " "   
}

FULL_DICT = {**BRAILLE_DICT, **NUMBER_DICT, **CHAR_DICT}

def is_braille(text):
   
    return all(c in "O." for c in text) and len(text) % 6 == 0

def translate_braille_to_english(braille_text):
    translated_text = ""
    i = 0
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        translated_text += FULL_DICT.get(braille_char, "?") 
        i += 6 
    return translated_text


def translate_english_to_braille(english_text):
    braille_text = ""
    for char in english_text:
        for key, value in FULL_DICT.items():
            if value == char:
                braille_text += key
                break
    return braille_text
def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate> [additional_strings...]")
        return

    # Combine all provided arguments into a single string
    input_text = " ".join(sys.argv[1:])

    if is_braille(input_text):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))

