########## EXTREME ##########
# Topics: Cryptography, Cypher #

# The function atbash is required to have that name for the challenge checker !! DO NOT CHANGE !!

# Cyphers, a basic form of enryption involve scrambling in a predictable way that means it can be retrieved
# The atbash cypher is a symmetric cypher meaning it uses the same algorithm / key to encrypt and decrypt
# In this case this means performing the cypher twice returns the original plaintext

# THE CHALLENGE - write a function which performs the atbash cypher
# The atbash cypher is a cypher which swaps letters in the alphabet with their opposite e.g. a becomes z, b becomes y etc...
# the function should accept capital letters
# the function should not change symbols or numbers, only upper and lowercase letters
# examples: abc -> zyx AbC123 -> ZyX123


def atbash(plaintext: str) -> str:
    return str()