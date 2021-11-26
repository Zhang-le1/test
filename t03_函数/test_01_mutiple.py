# 九九乘法表

def multiple_table():
    m = 1
    while m <= 9:
        n = 1
        while n <= m:
            print("%d*%d=%d" % (n, m, (m*n)), end="\t")
            n += 1
        print("")
        m += 1
