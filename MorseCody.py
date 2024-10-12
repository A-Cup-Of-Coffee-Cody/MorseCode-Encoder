# Description: This program reads in a text file and converts the text to Morse code. The Morse code is then converted to audio and saved as a WAV file.
# Author: Cody Tan
# Date: 2021-09-26

# Import libraries
import sys
import wave
import numpy as np

# Sound properties for 8 WPM
freq = 550  # Hz
dotLength = 200  # milliseconds (1 unit)
dashLength = dotLength * 3 
pauseBetweenSymbols = dotLength
pauseBetweenLetters = dotLength * 2
pauseBetweenWords = dotLength * 3 

# Get command line arguments
if len(sys.argv) != 2:
    print("Usage: python MorseCody.py <input file>")
    sys.exit(1)

# Read in the input file
inputFile = './Morse Code Test/' + sys.argv[1] + '.txt'
outputFile = './Morse Code Test/' + sys.argv[1] + ".wav"

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', 
    ',': '--..--', 
    '.': '.-.-.-', 
    '?': '..-.-', 
    '!': '-.-.--', 
    ':': '---...', 
    ';': '-.-.-.', 
    "'": '.----.', 
    '-': '-....-', 
    '_': '..--.-', 
    '"': '.-..-.', 
    '(': '-.--.', 
    ')': '-.--.-', 
    '&': '.-...', 
    '=': '-...-',
    '+': '.-.-.',
    ' ': '/', 
    '\n': '\n' 
}

# Function to convert text to Morse code
def textToMorseCode(text):
    morseCode = ''
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morseCode += MORSE_CODE_DICT[letter] + ' '
    return morseCode.strip()

# Read Alphanumeric File
try:
    with open(inputFile, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: The file '{inputFile}' does not exist.")
    sys.exit(1)

# Generate and save Morse audio as WAV

# Create a WAV file
with wave.open(outputFile, 'wb') as wf:
    wf.setnchannels(1)  # Mono
    wf.setsampwidth(2)  # 2 bytes for 16-bit PCM
    wf.setframerate(44100)  # Sample rate in Hz

    morse_code = textToMorseCode(text)
    
    # Generate audio samples for each Morse character
    for char in morse_code:
        if char == '.':
            # Create a dot sound
            samples = np.sin(2 * np.pi * np.arange(44100 * (dotLength / 1000)) * freq / 44100).astype(np.float32)
            wf.writeframes((samples * 32767).astype(np.int16).tobytes())
            # Pause between symbols
            samples = np.zeros(int(44100 * (pauseBetweenSymbols / 1000))).astype(np.float32)
            wf.writeframes((samples * 32767).astype(np.int16).tobytes())
        elif char == '-':
            # Create a dash sound
            samples = np.sin(2 * np.pi * np.arange(44100 * (dashLength / 1000)) * freq / 44100).astype(np.float32)
            wf.writeframes((samples * 32767).astype(np.int16).tobytes())
            # Pause between symbols
            samples = np.zeros(int(44100 * (pauseBetweenSymbols / 1000))).astype(np.float32)
            wf.writeframes((samples * 32767).astype(np.int16).tobytes())
        elif char == '/':
            # Pause for space between words
            samples = np.zeros(int(44100 * (pauseBetweenWords / 1000))).astype(np.float32)
            wf.writeframes((samples * 32767).astype(np.int16).tobytes())
        else:
            # Pause for space between letters
            samples = np.zeros(int(44100 * (pauseBetweenLetters / 1000))).astype(np.float32)
            wf.writeframes((samples * 32767).astype(np.int16).tobytes())

print(f"WAV file saved as: {outputFile}")