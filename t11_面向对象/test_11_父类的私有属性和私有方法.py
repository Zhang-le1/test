"""
    父类的 私有属性 和 私有方法
        1、子类对象不能在自己的方法内部，直接访问 私有属性 和 私有方法
        2、子类对象 可以通过父类的公有方法间接的访问到私有属性或私有方法
"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))


class B(A):
    def demo(self):
        # 1、在子类的对象方法中，不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)

        # 2、在子类的对象方法中，不能调用父类的私有方法
        # self.__test()
        pass


# 创建一个字子类对象
b = B()
print(b)
b.demo()

# 在外界不能直接访问对象的私有属性/调用私有方法
# # print(b.__num2)
# b.__test()
