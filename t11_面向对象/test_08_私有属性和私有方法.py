"""
    私有属性和私有方法
    应用场景：
        1、对象的某些属性或方法可能只希望在对象的内部被使用，而不是希望在外部被访问到
        2、私有属性就是对象不希望公开的属性
        3、私有方法就是对象不希望公开的方法
    定义方式：
        在定义属性或方法时，在属性或者方法名前增加两个下划线，定义的就是私有属性或方法
"""
"""
    伪私有属性和私有方法（不建议使用这种方式访问对象的稀有属性或私有方法）
    私有化的处理方式：
        在名称前加上 _类名，即 _类名__名称
"""


class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


XiaoFang = Women("小芳")

# 私有属性在外界不能被直接访问
# print(XiaoFang.__age)

# 私有方法，同样在外界不能被直接访问
XiaoFang._Women__secret()