
from q05 import c_n_gram

if __name__ == '__main__':
    text1 = "paraparaparadise"
    text2 = "paragraph"

    X = set(c_n_gram(2, text1))
    Y = set(c_n_gram(2, text2))

    uni_set = X | Y
    its_set = X & Y
    dif_set = X - Y

    print("union=", uni_set)
    print("intersection=", its_set)
    print("difference set=", dif_set)

    se = set()
    se.add(tuple('se'))
    print("'se' is subset of X?:", se.issubset(X))
    print("'se' is subset of Y?:", se.issubset(Y))
    # print(se.issubset(Y))
