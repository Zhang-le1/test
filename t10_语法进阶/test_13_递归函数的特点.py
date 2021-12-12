"""
    递归函数的特点
    特点：
        一个函数内部调用自己，函数内部可以调用其他函数，也可以调用自己
    代码特点：
        （1）函数内部的代码是相同的，只是针对参数不同，处理的结果不同
        （2）当参数满足一个条件时，函数不再执行，通常被称为递归的出口，否则会出现死循环
"""


def sum_number(num):
    print(num)
    # 递归的出口，当参数满足某个条件时，不再执行函数
    if num == 1:
        return
    # 自己调用自己
    sum_number(num - 1)


sum_number(3)


"""
    需求：
        定义一个函数sum_number
        能够接收一个num的整数参数
        计算1+2+...+num的结果
"""


def sum_sum(num1):
    # 出口
    if num1 == 1:
        return 1
    # 数字的累加
    temp = sum_sum(num1 - 1)

    return num1 + temp


result = sum_sum(3)
print(result)
