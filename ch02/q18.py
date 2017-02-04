# coding: utf-8

if __name__ == '__main__':
    col3 = {}
    with open('hightemp.txt', 'r') as f: #より安全なファイルの開き方
        lines = f.readlines() #1行ずつを要素とするリスト

    for i, line in enumerate(lines):
        ary_col = line.split('\t')
        col3[i] = ary_col[2]

    lines_sorted = "".join([lines[key] for key, value in sorted(col3.items(), key = lambda x:x[1], reverse=True)])
    print(lines_sorted)
