"""
    __del__ 方法，对象被从内存中销毁前，会被自动调用
    __str__ 方法，返回对象的描述信息，print 函数输出使用(设置自定义打印的内容)
    在python中，使用print输出对象变量，默认情况下，会输出这个变量引用的对象
    是由哪一个类创建的对象，以及在内存中的地址（十六进制表示）
"""


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫【%s】" % self.name


cat = Cat("Tom")
print(cat.name)
print(cat)
print("-" * 50)
