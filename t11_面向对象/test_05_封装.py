"""
    1、封装是面向对象编程的一大特点
    2、面向对象编程的第一步————将属性和方法封装到一个抽象的类中
    3、外界使用类创建对象，然后让对象调用方法
    4、对象方法的细节都被封装在类的内部
    5、在对象的方法内部，可以直接访问对象的属性
    6、同一个类创建的多个对象之间，属性互不干扰
"""

"""
    需求：
        1、小明体重75.0公斤
        2、小明每次跑步会减肥0.5公斤
        3、小明每次吃东西体重会增加1公斤
"""


class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 % s 体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()

print(xiaoming)
