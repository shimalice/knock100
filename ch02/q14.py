# coding: utf-8
import sys

def output_n(f, n):
    with open(f, 'r') as f:
        lines = f.readlines()[:n]
        n_lines = "".join(lines)
        print(n_lines)

if __name__ == '__main__':
    output_n('hightemp.txt', int(sys.argv[1]))
