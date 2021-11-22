"""
    从控制台输入要出的拳——石头1、剪刀2、布3
    电脑 随机 出拳，先假定电脑只会出石头，完成整体代码功能
    比较胜负
"""
# 在导入工具包的时候，应该将导入的文件放在顶部
import random

player = int(input("请输入要出的拳 石头1、剪刀2、布3："))
print("玩家选择的拳头是 %d" % player)

computer = random.randint(1, 3)
print("玩家出的拳是%d,电脑出的拳是 %d" % (player, computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("电脑弱爆了！！！")
elif player == computer:
    print("真是棋逢对手，平局！！！")
else:
    print("真菜，呆脑都打不赢！！！")
