def alphabet_position(text):
    text=text.lower()
    text=''.join(e for e in text if e.isalnum())
    d={'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6,
    'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15,
    'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21,
    't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    s=""
    for i in range(len(text)):
        s=s+str(d[text[i]])+" "
    return s[:len(s)-1]
    pass