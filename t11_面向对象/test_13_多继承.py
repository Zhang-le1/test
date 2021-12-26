"""
    多继承
        子类可以拥有多个父类，并且具有所有父类的属性和方法
"""


class A:
    def test(self):
        print("A类的test方法")


class B:
    def demo(self):
        print("B类的demo方法")


# C类多继承
class C(A, B):

    pass


# 创建子类对象
c = C()
c.test()
c.demo()
# 内置属性 __mro__ 可以查看 方法搜索顺序
print(C.__mro__)
