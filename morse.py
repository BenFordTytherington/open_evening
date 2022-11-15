########## HARD / EXTREME ##########
# Topics: Encoding, Dictionaries #

# The functions to_morse and from_morse are required to have that name for the challenge checker !! DO NOT CHANGE !!

# INFORMATION:
# Morse code is a system of encoding alphabetic characters into a series of dots and dashes
# this can be represented as 1s and 0s or as . and - sequences

# Encoding:
# A =>  .-      # N =>  -.
# B =>  -...    # O =>  ---
# C =>  -.-.    # P =>  .--.
# D =>  -..     # Q =>  --.-
# E =>  .       # R =>  .-.
# F =>  ..-.    # S =>  ...
# G =>  --.     # T =>  -
# H =>  ....    # U =>  ..-
# I =>  ..      # V =>  ...-
# J =>  .---    # W =>  .--
# K =>  -.-     # X =>  -..-
# L =>  .-..    # Y =>  -.--
# M =>  --      # Z =>  --..

# THE CHALLENGE - create 2 functions, one to encode and one to decode from morse strings of dot and dash
# The functions should return strings, morse strings whould have letters separated with a space and plain strings don't need spaces between words
# The functions should convert all text to lowercase to convert

# BONUS - make both the functions in a single line each
# DOUBLE BONUS - make the function compatible with binary literals instead e.g B => -... => 1000 and X => -..- => 1001

# not necessary for the challenge checker but you may find it helpful
_to = {
    'a': '.-', 'b': '-...',
    'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....',
    'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.',
    's': '...', 't': '-',
    'u': '..-', 'v': '...-',
    'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
}

_from = {}

def to_morse(plaintext: str) -> str:
    return str()

def from_morse(morse: str) -> str:
    return str()