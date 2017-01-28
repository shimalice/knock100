 # coding: utf-8

 if __name__ == '__main__':
    col1 = open('col1.txt', 'r')
    col2 = open('col2.txt', 'r')

    with col1, col2:
        ary_col1 = col1.readlines
        ary_col2 = col2.readlines
        m_col12 = "\n".join([e_col1+"\t"+e_col2 for e_col1, e_col2 in ary_col1, ary_col2])

    with open('m_col.txt', 'w') as m_col:
        m_col.write(m_col12)
