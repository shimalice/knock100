# coding: utf-8

def cipher(text):
    return ''.join([chr(219 - ord(char)) if char.islower() else char for char in text])

if __name__ == '__main__':
    text = 'Shimalice' #=>

    ciph_text = cipher(text)
    print(ciph_text)
    origin_text = cipher(ciph_text)
    print(origin_text)
