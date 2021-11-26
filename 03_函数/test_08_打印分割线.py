def print_line():
    """需求1：定义一个 print_line 函数能够打印*组成的一条分割线"""

    print("*" * 50)


print_line()


def print_line2(char):
    """需求2：定义一个函数能打印任意字符组成的分割线"""
    print(char * 50)


print_line2("-")


def print_line3(char, times):
    """需求3：定义一个函数能打印任意重复次数的分割线"""
    print(char * times)


print_line3("+", 20)
