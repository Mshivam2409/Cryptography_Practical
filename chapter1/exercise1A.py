# import chapter1 as ch1
# from chapter1 import encode
# f = open("jane_austen.txt", "r")
# text = f.read()
# encoding, decoding = ch1.create_shift_substitutions(6)
# encoded = encode(text.upper(), encoding)
# f = open("jane_austen_decoded.txt", "w")
# f.write(text.upper())
# f.close()
import string
from chapter1 import create_shift_substitutions, decode
import enchant

def decode_cipher(text):
    dictionary = enchant.Dict('en')
    final_text = text
    prev_hits = 0
    for n in range(0,len(string.ascii_uppercase)):
        encoding,decoding = create_shift_substitutions(n)
        decoded_text = decode(text,decoding)
        decoded_words = decoded_text.split(" ")
        hits = 0
        for word in decoded_words:
            hits += dictionary.check(word)
        if hits>prev_hits:
            prev_hits = hits
            final_text = "".join((word + " ") for word in decoded_words)
    return final_text

if __name__ == "__main__":
    f = open("jane_austen_encoded.txt", "r")
    text = f.read()
    f = open("decoded.txt", "w")
    f.write(decode_cipher(text))
    f.close()