# coding: utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f: #より安全なファイルの開き方
        f_size = len(f.readlines()) #1行ずつを要素とするリスト
    print(f_size)
