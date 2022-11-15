from itertools import permutations
from hashlib import sha256

########## EXTREME ##########
# Topics: Security, Permutations, Hashing, Hexadecimal #

# The variable password is required to have that name for the challenge checker !! DO NOT CHANGE !!
# The variable secret_password contains the hashed value of the real password, !! DO NOT CHANGE !!

# INFORMATION:
# Brute force attacks are attacks which try every possible password in an input field to find the correct one
# They require a huge amount of computing power to crack a strong password as increasing the length of the password dramatically increases the number of possible outcomes
# This is due to permutations being proportional to factorials
# for example, a password using only lowercase letters (a set of 26 possible) and 3 characters
# has 15600 permutations (26 P 3)
# but increasing the set to lowercase, uppercase and numbers (a set of 62 possible) and 5 characters,
# has 776520240 permutations
#
# !! IMPORTANT !!
# The secret password is 4 characters and contains lowercase, uppercase and numbers
# it is stored as an integer of the hashed value
# so for the password = '...'
# the stored password (check.secret_password) is sha256(password).hexdigest() converted to an integer
# your answer should be an integer
# useful functions for this include:
# str.encode() to return a bytes object
# sha256(bytes).hexdigest() to return a string of hexadecimal characters for the hash of bytes input
# int('hexadecimal string', 16) to convert from base 16

# THE CHALLENGE - create a function which can crack the password stored in check.py

# WARNING:
# the function will likely take upwards of 2 minutes to crack the password so don't be alarmed if the function causes a brief freeze

# TIPS:
# Consider using itertools.permutations(set, length) to generate all possible permutations of a set with given length
# e.g. permutations('abcdefghijklmnopqrstuvwxyz', 3) will generate all lowercase strings of 3 letters


def brute_force():
    return str()

secret_password = 0x83010c9161ad0a37d408d7198b3d2daa95d89cca9cd0e82ec0c92298745d941d

password = brute_force()