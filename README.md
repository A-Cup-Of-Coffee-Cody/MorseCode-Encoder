# Morse Code Audio Converter

This program reads a text file containing alphanumeric characters and converts the text into Morse code. The resulting Morse code is then converted into audio, which is saved as a WAV file.

## Author

Cody Tan  
Date: September 26, 2021

## Prerequisites

Before running this program, ensure you have the following installed:

- Python 3.x
- Required libraries:
  - `numpy`
  - `wave`

You can install the required libraries using pip:

```bash
pip install numpy
```

# Usage

1. Prepare a text file containing the text you wish to convert. Ensure that it only contains alphanumeric characters and some special symbols supported by the Morse code dictionary.

2. Save your text file in the ./Morse Code Test/ directory.

3. Run the program from the command line, providing the name of the text file (without the .txt extension) as a command line argument. For example:

```bash
python MorseCody.py <input_file>
```

Replace <input_file> with the name of your text file. For example, if your file is named example.txt, you would run:

```bash
python MorseCody.py example
```

# How It Works

- The program defines a dictionary that maps characters to their Morse code equivalents.

- It reads the content of the specified text file.

- The text is converted to Morse code using the textToMorseCode function.

- The Morse code is then translated into audio signals:

  - A dot (.) is represented by a short beep.
  - A dash (-) is represented by a longer beep.
  - Spaces between symbols, letters, and words are represented by silence.

- The audio is saved as a WAV file in the same directory as the input text file with the same base name but with a .wav extension.

# Output

The output WAV file will be saved in the ./Morse Code Test/ directory with the same base name as the input file. For example, if the input file is example.txt, the output will be example.wav.

## Morse Code Dictionary

The program supports the following characters in Morse code:

| Character | Morse Code | Character | Morse Code |
| --------- | ---------- | --------- | ---------- |
| A         | .-         | N         | -.         |
| B         | -...       | O         | ---        |
| C         | -.-.       | P         | .--.       |
| D         | -..        | Q         | --.-       |
| E         | .          | R         | .-.        |
| F         | ..-.       | S         | ...        |
| G         | --.        | T         | -          |
| H         | ....       | U         | ..-        |
| I         | ..         | V         | ...-       |
| J         | .---       | W         | .--        |
| K         | -.-        | X         | -..-       |
| L         | .-..       | Y         | -.--       |
| M         | --         | Z         | --..       |
| 1         | .----      | 6         | -....      |
| 2         | ..---      | 7         | --...      |
| 3         | ...--      | 8         | ---..      |
| 4         | ....-      | 9         | ----.      |
| 5         | .....      | 0         | -----      |
| ,         | --..--     | :         | ---...     |
| .         | .-.-.-     | ;         | -.-.-.     |
| ?         | ..-.-      | '         | .----.     |
| !         | -.-.--     | -         | -....-     |
| \_        | ..--.-     | "         | .-..-.     |
| (         | -.--.      | )         | -.--.-     |
| &         | .-...      | =         | -...-      |
| +         | .-.-.      | (space)   | /          |

# Error Handling

- If the specified input file does not exist, an error message will be displayed, and the program will terminate.

# License

This project is open-source and available for personal and educational use. For any other uses, please contact the author.

```kotlin
Feel free to copy this and use it in your project!
```
