"""
    元组和字典的拆包
    1、在调用带有多值参数的函数时，如果希望：
        将一个元组变量，直接传递给 args
        将一个字典变量，直接传递给 kwargs
    2、可以使用拆包，简化参数的传递，拆包的方式是：
        在元组变量前，增加一个 *
        在字典变量前，增加两个 *
"""


# 拆包
def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": "18"}


demo(*gl_nums, **gl_dict)
