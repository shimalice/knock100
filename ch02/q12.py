# coding: utf-8

if __name__ == '__main__':
    col1 = []
    col2 = []
    with open('hightemp.txt', 'r') as f: #より安全なファイルの開き方
        lines = f.readlines() #1行ずつを要素とするリスト

    for line in lines:
        ary_col = line.split('\t')
        col1.append(ary_col[0])
        col2.append(ary_col[1])
    # print(col1)

    with open('col1.txt', 'w') as col1_text:
        for ary_col1 in col1:
            col1_text.write(ary_col1 + "\n")

    with open('col2.txt', 'w') as col2_text:
        for ary_col2 in col2:
            col2_text.write(ary_col2 + "\n")
