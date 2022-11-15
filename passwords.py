from base64 import b64encode
from hashlib import sha256

########## EXTREME ##########
# Topics: Cryptography, Hashing, CyberSecurity #

# The variables username, password, encoded_username and encoded_password are required to have that name for the challenge checker !! DO NOT CHANGE !!


# BACKGROUND:
# Passwords / login details stored in a database should NEVER be stored as plaintext
# in case of database breach by a hacker. This is why passwords are often stored as hashes,
# which is a sort of irreversible encryption which has a fixed length, unique value,
# and then the entered password has the same process applied and is checked against the stored value.

# THE CHALLENGE - encode the username and password into base64 and hash them using sha256 and store those in encoded_password and encoded_username respectively

# The strings which you need to encode - value can be changed but not the variable name
username = 'johnsmith1971'
password = 'Password123'


def encode_and_hash(string: str) -> bytes:
    return bytes()

# the username and password should be encoded into base64 and hashed using sha256
encoded_username: bytes = b''
encoded_password: bytes = b''
