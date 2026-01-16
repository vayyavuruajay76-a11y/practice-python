def is_isogram(string):
    return True if len(''.join(e for e in string if e.isalpha()).lower()) == len(set(''.join(e for e in string if e.isalpha()).lower())) else False
