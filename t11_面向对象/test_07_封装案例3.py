"""
    封装：
        1、封装是面向对象编程的一大特点
        2、面向对象编程的第一步：将属性和方法封装到一个抽象的类中
        3、外界使用类创建对象，然后让对象调用方法
        4、对象方法的细节都被封装在类的内部

        一个对象的属性可以是另外一个类创建的对象
"""
"""
    需求：
        1、士兵许三多有一把AK47
        2、士兵可以开火
        3、枪能够发射子弹
        4、枪装填子弹————增加子弹数量
"""


# 创建枪类
class Gun:
    def __init__(self, model):
        # 1、枪的型号
        self.model = model
        # 2、子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1、判断子弹的数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了" % self.model)
            return
        # 2、发射子弹, -1
        self.bullet_count -= 1
        # 3、提示发射信息
        print("[%s]突突突...[%d]" % (self.model, self.bullet_count))


# 创建士兵了类
class Soldier:
    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪  新兵没有枪
        # 在定义属性时，如果不知道设置什么初始值，可以设置为None
        self.gun = None


# 1、创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(4)
ak47.shoot()

# 2、创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47

print(xusanduo.gun)
