import string
from random import shuffle
def create_cryptogram():
    encoding = {}
    decoding = {}
    temp = [letter for letter in string.ascii_uppercase]
    shuffle(temp)
    for i in range(0,len(temp)):
        encoding[string.ascii_uppercase[i]] = temp[i]
        decoding[temp[i]] = string.ascii_uppercase[i]
    return encoding,decoding

def print_substitution():
    encoding, _ = create_cryptogram()
    en = "".join((letter+" ") for letter in encoding)
    sb = "".join((encoding.get(letter)+" ") for letter in encoding)
    return "{}\n{}".format(en, sb)
    
if __name__ == "__main__":
    print(print_substitution())