# coding: utf-8
import sys

def divide(f, n):
    with open(f, 'r') as f:
        r_lines = f.readlines()
    for i in range(0, len(r_lines), n):
        out_fname = "out_f" + str(i)
        with open(out_fname, 'w') as out_f:
            n_lines = "".join(r_lines[i:i+n])
            out_f.write(n_lines)

if __name__ == '__main__':
    divide('hightemp.txt', int(sys.argv[1]))
