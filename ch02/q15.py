# coding: utf-8
import sys

def output_n_i(f, n):
    with open(f, 'r') as f:
        r_lines = f.readlines()[-n:]
        n_lines = "".join(r_lines)
        print(n_lines)

if __name__ == '__main__':
    output_n_i('hightemp.txt', int(sys.argv[1]))
