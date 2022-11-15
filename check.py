import skyline
import passwords
import databases
import atbash as atb
import farey
import morse
import brute
from scope import st, s, m, g, n, func

from base64 import b64encode
from hashlib import sha256
import sqlite3 as sql
import types
import ast

### Check Functions ###
def get_average_height(skyline_matrix: list) -> float:
    try:
        number_of_columns = len(skyline_matrix[0])
        cumulative_height = 0

        for row_index in range( len(skyline_matrix ) ):
            cumulative_height += sum(skyline_matrix[row_index])

        return cumulative_height / number_of_columns

    except:
        return None


def encode_hash(string: str) -> bytes:
    try:
        b64 = b64encode(string.encode())
        return sha256(b64).digest()
    
    except:
        return None


def execute_query(query):
    with sql.connect('data.db') as conn:
        c = conn.cursor()
        result = c.execute(query).fetchall()
        c.close()
        conn.commit()

    return result


def get_users() -> list:
    arr = execute_query(
        '''
        SELECT username, first_name from users WHERE age > 27 ORDER BY age ASC;
        '''
    )
    return arr


def atbash(plaintext: str) -> str:
    chars = []
    lower = 97
    upper = 65
    for char in plaintext:
        if ord(char) >= lower:
            diff = ord(char) - lower
            chars.append(
                chr(
                    (lower + 25) - diff
                )
            )

        elif ord(char) >= upper:
            diff = ord(char) - upper
            chars.append(
                chr(
                    (upper + 25) - diff
                )
            )

        else:
            chars.append(char)

    return ''.join(chars)


def farey_sequence(order: int) -> set:
    s = set()
    for denominator in range(1, order + 1):
        for numerator in range(0, denominator + 1):
            s_vals = {x[2] for x in s}
            if numerator / denominator not in s_vals:
                s.add((numerator, denominator, numerator / denominator))

    return sorted(s, key=lambda t: t[2])

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

_from = {_to[key]: key for key in _to.keys()}

to_morse = lambda plain: ' '.join([_to.get(char) if _to.get(char) else char for char in plain.lower()])
from_morse = lambda morse: ''.join([_from.get(string) if _from.get(string) else string for string in morse.split(' ')])


def locals_globals():
    for o, t in ((m, dict), (st, str), (s, set), (g, types.GeneratorType), (n, None)):

        if not (o is None or isinstance(o, t)):
            return False

    lcls = func.__code__.co_consts
    t = (bool, int, float, list, tuple, bytes, bytearray, memoryview)

    for i in lcls:
        if type(i) not in t and i:
            return False

    return True


with open('test.py', 'r') as f:
    src = f.read()

code = ast.parse(src)

expressions = [exp for exp in ast.walk(code)]
expressions.pop(0)


def has_construct(t: type, arr: list):
    def wrapper():
        for node in arr:
            if isinstance(node, t):
                return True

        return False

    return wrapper


has_while = has_construct(ast.While, expressions)
has_for = has_construct(ast.For, expressions)
has_if = has_construct(ast.If, expressions)

def get_funcs(arr: list):
    funcs = []
    for node in arr:
        if isinstance(node, ast.Call):
            funcs.append(node)

    return funcs

funcs = get_funcs(expressions)


### Boilerplate ###


class Challenge:
    def __init__(self, name: str, condition: bool, points: int):
        self.name = name
        self.condition = condition
        self.points = points


def check_completed(challenge: Challenge) -> None:
    global points

    if challenge.condition:
        print(f'challenge: {challenge.name} completed!')
        points += challenge.points

    else:
        print(f'challenge {challenge.name} not completed :(')

p = 'hX8g'
challenges = [
    Challenge(
        'skyline', 
        (skyline.avg_height == get_average_height(skyline.skyline) ),
        1
    ),
    Challenge(
        'passwords', 
        (passwords.encoded_username == encode_hash(passwords.username) and passwords.encoded_password == encode_hash(passwords.password)),
        2
    ),
    Challenge(
        'databases', 
        (databases.users == get_users()),
        2
    ),
    Challenge(
        'atbash', 
        (atb.atbash('ABCabc123!') == atbash('ABCabc123!')),
        3
    ),
    Challenge(
        'farey', 
        (farey.farey(9) == farey_sequence(9)),
        3
    ),
    Challenge(
        'morse', 
        (morse.to_morse('hello world 123') == to_morse('hello world 123') and morse.from_morse('.... . .-.. .-.. ---   .-- --- .-. .-.. -..   1 2 3') == 'helloworld123'),
        2
    ),
    Challenge(
        'brute', 
        (brute.password == p),
        1
    ),
    Challenge(
        'scope', 
        (locals_globals()),
        1
    ),
]

points = 0
if __name__ == '__main__':
    for challenge in challenges:
        check_completed(challenge)

    print(f'scored {points} points')

