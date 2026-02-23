import string
mapping=dict(zip(list("abcdefghijklmnopqrstuvwxyz"),list("zyxwvutsrqponmlkjihgfedcba")))
def encode(plain_text):
    cipher = ""
    for ch in plain_text.lower():
        if ch in mapping.keys():
            cipher += mapping[ch]
        elif ch in string.punctuation:
            continue
        else:
            cipher += ch
    c = ''.join(cipher.split())
    return " ".join(c[i:i+5] for i in range(0, len(c), 5))


def decode(ciphered_text):
    plain_text = ""
    for ch in ''.join(ciphered_text.split()):
        if ch in mapping.values():
            plain_text += mapping[ch]
        else:
            plain_text += ch
    return plain_text
