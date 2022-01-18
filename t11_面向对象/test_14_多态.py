"""
    多态
    面向对象三大特性：
    1.封装 根据职责将属性和方法封装到一个抽象的类中
    2.继承 实现代码的重用，相同的代码不需要重复的编写
    3.多态 不同的子类对象调用相同的父类方法没产生不同的执行结果
        多态可以增加代码的灵活度
        以继承和重写父类方法为前提
        是调用方法的技巧，不会影响到类的内部设计
"""
"""
    需求：
    1.在 Dog 类中封装方法 game
        普通狗只是简单的玩耍
    2.定义 XiaoTianQuan 继承自 Dog ，并且重写方法 game
        哮天犬需要在天上玩耍
    3.定义 Person 类，并且封装一个 和狗玩 的方法
        在方法内部，直接让 狗对象 调用 game方法
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍。。。" % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s 飞到天上去玩耍。。。" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1.创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianQuan("飞天旺财")
# 2.创建一个小明对象
xiaoming = Person("小明")

# 3.让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
