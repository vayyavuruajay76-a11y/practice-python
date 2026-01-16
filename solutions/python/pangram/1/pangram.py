def is_pangram(sentence):
    
    # abcdefghijklmnopqrstuvwxyz
    alphahastr = "abcdefghijklmnopqrstuvwxyz"
    alphaset = set(alphahastr)
    finalstr = set(''.join(e for e in sentence if e.isalpha()).lower())
    if(len(alphaset)==len(finalstr)):
        return True
    else:
        return False
