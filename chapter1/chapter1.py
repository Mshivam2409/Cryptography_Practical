import string


def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subs_letter = string.ascii_uppercase[(i+n) % alphabet_size]
        encoding[letter] = subs_letter
        decoding[subs_letter] = letter
    return encoding, decoding


def encode(message, substn):
    cipher = ""
    for x in message:
        if x in substn:
            cipher = cipher + substn[x]
        else:
            cipher += x
    return cipher


def decode(message, encod):
    return encode(message, encod)


def print_substitution(n):
    encoding, _ = create_shift_substitutions(n)
    en = "".join((letter+" ") for letter in encoding)
    sb = "".join((encoding.get(letter)+" ") for letter in encoding)
    return "{}\n{}".format(en, sb)
