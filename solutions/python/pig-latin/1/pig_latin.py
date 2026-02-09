def translate(text):
    def translate_word(word):
        vowels = "aeiou"
        
        # Rule 1: Starts with vowel, xr, or yt
        if word[0] in vowels or word.startswith(("xr", "yt")):
            return word + "ay"
        
        # Rule 3: Consonants + "qu"
        # Find the index of 'qu' and check if consonants precede it
        qu_index = word.find("qu")
        if qu_index != -1:
            # Verify everything before 'qu' is a consonant
            before_qu = word[:qu_index]
            if all(char not in vowels for char in before_qu):
                return word[qu_index + 2:] + word[:qu_index + 2] + "ay"

        # Rules 2 & 4: Move consonants until first vowel or 'y'
        for i in range(len(word)):
            # 'y' counts as a vowel ONLY if it's not the first letter
            if word[i] in vowels or (i > 0 and word[i] == 'y'):
                return word[i:] + word[:i] + "ay"
        
        return word + "ay"

    # Split the sentence, translate each word, and rejoin
    return " ".join(translate_word(w) for w in text.split())