"""
    需求：
        小猫爱吃鱼，小猫要喝水
    分析：
        定义一个猫类
        定义两个方法 eat 和 drink
        创建猫对象
"""


class Cat:

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 在日常开发中，不推荐在类的外部给对象增加属性
# 如果在运行时，没有找到属性，程序会报错
# 对象的属性应该封装在类的内部
# tom.name = "TOM"
tom.eat()
tom.drink()
tom.name = "TOM"
