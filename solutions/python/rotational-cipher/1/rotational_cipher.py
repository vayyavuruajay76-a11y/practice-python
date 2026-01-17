import string
def rotate(text, key):
    cipher=''
    for x in text:
        if x in string.ascii_lowercase:
            cipher += chr(((ord(x)+key)-97) % 26+97)
        elif x in string.ascii_uppercase:
            cipher += chr(((ord(x)+key)-65) % 26+65)
        else:
            cipher += x
    return cipher
