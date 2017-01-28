# coding: utf-8

from random import shuffle

def typoglycemia(text):
    words = text.split()
    typo_words = []

    for word in words:
        if len(word) > 5:
            s_char = word[0]
            e_char = word[-1]
            b_chars = list(word[1:-1])
            shuffle(b_chars)
            typo_words.append(''.join([s_char, ''.join(b_chars), e_char]))
        else:
            typo_words.append(word)

    return ' '.join(typo_words)

if __name__ == '__main__':
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    typo_text = typoglycemia(text)

    print(typo_text)
