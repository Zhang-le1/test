"""
    需求：
        1、房子（House）有户型、总面积和家具名称列表
            新房子没有任何的家具
        2、家具（HouseItem）有名字和占地面积，其中：
            席梦思（bed） 占地 4平米
            衣柜（chest） 占地2平米
            餐桌（table） 占地1.5平米
        3、将以上三件家具添加到房子中
        4、打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
"""


class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f平米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)
        # 1、判断家具的面积是否超过剩余面积，如果超过，提示不能添加这件家具
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
            return

        # 2、将家具的名称追加到家具名称列表中
        self.item_list.append(item.name)

        # 3、用房子的剩余面积 - 家具面积
        self.free_area -= item.area


# 创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 20)

print(bed)
print(chest)
print(table)

# 2、创建房子对象
my_house = House("两室一厅", 60)

my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)
