# coding: utf-8

if __name__ == '__main__':
    set_col1 = set()
    with open('hightemp.txt', 'r') as f: #より安全なファイルの開き方
        lines = f.readlines() #1行ずつを要素とするリスト

    for line in lines:
        set_col1.add(line.split('\t')[0])

    print(set_col1)
