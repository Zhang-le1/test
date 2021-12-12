"""
    多值参数
    1、有时候可能需要一个函数能处理的参数个数是不确定的，这时就可以使用多值参数
        （1）参数名前增加一个 * 可以接收 元组
        （2）参数名前增加两个 * 可以接收 字典
    2、一般在给多值参数命名时，习惯使用以下：
        （1）*args  存放元组参数，前面一个*
        （2）**kwargs  存放字典参数，前面两个*
"""


def demo(num, *nums, **numss):
    print(num)
    print(nums)
    print(numss)


demo(1)
demo(1, 2, 3, 4, 5, name="小明", age="18")


"""
    需求：
    定义一个函数 sum_number 可以接收任意多个整数
    并将传递的所有数字累加，且返回累加结果
"""


def sum_number(*args):
    num = 0
    for n in args:
        num += n
    return num


print(sum_number(1, 2, 3))
