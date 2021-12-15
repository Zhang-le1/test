"""
    初始化方法
        当使用 类名（） 创建对象时，会自动执行以下操作
        1、为对象在内存中分配空间--创建对象
        2、为对象的属性设置初始值--初始化方法（init）

        这个初始化方法就是 __init__ 方法，__init__ 是对象的内置方法
        __init__ 方法是专门用来定义一个类具有哪些属性的方法
"""
"""
    如果希望在 创建对象的同时，就设置对象的属性，可以对 __init__ 方法进行改造
    1、把希望设置的属性值，定义成 __init__ 方法的参数
    2、在方法内部使用 self.属性 = 形参 接收外部传递的参数
    3、在创建对象时，使用 类名（属性1，属性2）调用
"""


class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用 类名（） 创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")

print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
