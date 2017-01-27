# coding: utf-8

def tempar(x, y, z):
    return "%(x)s時の%(y)sは%(z)s" % locals()

if __name__ == '__main__':
    x = 12
    y = '気温'
    z = 22.4

    text = tempar(x, y, z)
    print(text)
