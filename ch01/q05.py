
def w_n_gram(n, seq):
    w_gram = []
    words = ["<s>"] + seq.split()
    words.append("</s>")
    for i in range(len(words) - n + 1):
        w_gram.append(words[i:i+n])

    return w_gram

def c_n_gram(n, seq):
    c_gram = []
    for i in range(len(seq) - n + 1):
        # if seq[i] == " " or seq[i+1] == " ": continue
        c_gram.append(tuple(seq[i:i+n]))

    return c_gram

if __name__ == '__main__':

    text = 'I am an NLPer'
    print(w_n_gram(2, text))
    print(c_n_gram(2, text))
