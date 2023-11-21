from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

morse_code = {
    'A': ['.-', 2],
    'B': ['-...', 3],
    'C': ['-.-.', 3],
    'D': ['-..', 3],
    'E': ['.', 1],
    'F': ['..-.', 3],
    'G': ['--.', 3],
    'H': ['....', 4],
    'I': ['..', 2],
    'J': ['.---', 4],
    'K': ['-.-', 3],
    'L': ['.-..', 4],
    'M': ['--', 2],
    'N': ['-.', 2],
    'O': ['---', 3],
    'P': ['.--.', 4],
    'Q': ['--.-', 4],
    'R': ['.-.', 3],
    'S': ['...', 3],
    'T': ['-', 1],
    'U': ['..-', 3],
    'V': ['...-', 4],
    'W': ['.--', 3],
    'X': ['-..-', 4],
    'Y': ['-.--', 4],
    'Z': ['--..', 4],
}

def blink_morse_code(letter):
    code, gap = morse_code[letter]
    for symbol in code:
        if symbol == '.':
            pin.on()
            sleep(0.2)
            pin.off()
            sleep(0.2)
        elif symbol == '-':
            pin.on()
            sleep(0.8)
            pin.off()
            sleep(0.2)
    sleep(gap)  # Gap between letters

print("LED starts flashing the alphabet in Morse code...")
while True:
    try:
        for letter in morse_code:
            blink_morse_code(letter)
    except KeyboardInterrupt:
        break

pin.off()
print("Finished.")
