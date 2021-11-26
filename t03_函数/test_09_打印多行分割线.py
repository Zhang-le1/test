def print_line3(char, times):
    """打印单行分隔符

    :param char: 分割字符
    :param times: 字符重复次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char: 分割线使用的分割字符
    :param times: 分割符重复的次数
    """
    row = 0
    while row < 5:
        print_line3(char, times)
        row += 1


print_lines("+", 50)
