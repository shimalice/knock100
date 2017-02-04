# coding: utf-8
import collections

if __name__ == '__main__':
    freq_col1 = collections.defaultdict(int)
    with open('hightemp.txt', 'r') as f: #より安全なファイルの開き方
        lines = f.readlines() #1行ずつを要素とするリスト

    for line in lines:
        ary_col = line.split('\t')
        freq_col1[ary_col[0]] += 1

    for key, value in sorted(freq_col1.items(), key = lambda x:x[1], reverse=True):
        print(value, key)
