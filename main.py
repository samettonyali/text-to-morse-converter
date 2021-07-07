
DICTIONARY = {
    'A': '.-',
    'a': '.-',
    'B': '-...',
    'b': '-...',
    'C': '-.-.',
    'c': '-.-.',
    'D': '-..',
    'd': '-..',
    'E': '.',
    'e': '.',
    'F': '..-.',
    'f': '..-.',
    'G': '--.',
    'g': '--.',
    'H': '....',
    'h': '....',
    'I': '..',
    'i': '..',
    'J': '.---',
    'j': '.---',
    'K': '-.-',
    'k': '-.-',
    'L': '.-..',
    'l': '.-..',
    'M': '--',
    'm': '--',
    'N': '-.',
    'n': '-.',
    'O': '---',
    'o': '---',
    'P': '.--.',
    'p': '.--.',
    'Q': '--.-',
    'q': '--.-',
    'R': '.-.',
    'r': '.-.',
    'S': '...',
    's': '...',
    'T': '-',
    't': '-',
    'U': '..-',
    'u': '..-',
    'V': '...-',
    'v': '...-',
    'W': '.--',
    'w': '.--',
    'X': '-..-',
    'x': '-..-',
    'Y': '-.--',
    'y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}


def convert_into_morse(text):
    for letter in text:
        if letter == " ":
            print(" ")
        else:
            print(DICTIONARY[letter])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = input("Please enter your string: ")
    convert_into_morse(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
