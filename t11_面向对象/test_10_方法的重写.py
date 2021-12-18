"""
    方法的重写
    当父类的方法实现不能满足需求时，可以对方法进行重写，有两种方法
    1、覆盖父类的方法
        在子类中重写编写父类的方法，即在子类中定义一个和父类同名的方法并且实现
        重写后，运行时，只会调用子类中重写的方法么不会调用父类封装的方法
    2、对父类方法进行扩展(子类的方法实现中包含父类的方法实现)
        在子类中重写父类的方法
        在需要的位置使用 super().父类方法 来调用父类方法的执行
        代码的其他位置针对子类的需求，编写子类特有的代码实现

"""


class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

# 1、覆盖父类的方法
# 如果子类中，重写的父类中的方法
# 在使用子类调用方法时，会调用子类中重写的方法
    # def bark(self):
    #     print("叫的跟神一样...")

# 2、对父类方法进行扩展
    def bark(self):
        # （1）针对子类特有的需求，编写代码
        print("神一样的叫声...")
        # （2）使用 super(). 调用原本在父类中封装的方法
        super().bark()
        # （3）增加其他子类的代码
        print("$^%$^%$^%^$%")


xtq = XiaoTianQuan()
xtq.bark()
