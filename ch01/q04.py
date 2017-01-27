if __name__ == '__main__':
    text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

    elements = text.replace(',', '').replace('.', '').split()

    res = dict([(element[0], i+1) if i in (0, 4, 5, 6, 7, 8, 14, 15, 18) else (element[:2], i+1) for i, element in enumerate(elements)])

    print(res)
