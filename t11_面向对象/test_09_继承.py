"""
    继承（单继承、多继承）
    1、封装：根据职责将属性和方法封装到一个抽象的类中
    2、继承：实现代码的重用，相同的代码不需要重复的编写
    3、多态：不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度
"""
"""
    继承的概念：子类拥有父类所有的属性和方法
    继承的语法：
    class 类名（父类名）：
        pass
    1、子类继承自父类，可以直接享受父类中已经封装好的方法
    2、子类中应该根据自身需要，封装子类特有的属性和方法
"""


# Dog 类是 Animal 类的子类，Animal类是Dog类的父类，Dog类从Animal类继承
# Dog 类是 Animal 类的派生类，Animal类是Dog类的基类，Dog类从Animal类派生
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


XiaoHuang = Dog()
XiaoHuang.eat()
XiaoHuang.drink()
XiaoHuang.run()
XiaoHuang.sleep()
XiaoHuang.bark()

# 继承的传递性(子类拥有父类及父类的父类的属性和方法)
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()
