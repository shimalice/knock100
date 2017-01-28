# coding: utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f: #より安全なファイルの開き方
        line = f.read() #1行ずつを要素とするリスト
    r_line = line.replace('\t', ' ')
    print(r_line)
