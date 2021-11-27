"""
    字典的定义
    1、dictionary（字典）是除列表以外最灵活的数据类型
    2、字典同样可以用来存储多个数据
        通常用来存储描述一个物体的相关信息
    3、和列表的区别：
        列表是有序的对象集合
        字典是无序的对象集合
    4、字典用{}定义
    5、字典使用键值对存储数据，键值对之间使用 ，分隔
        键 key 是索引
        值 value 是数据
        键和值之间使用 ： 分隔
        键必须是唯一的
        值可以取任何数据类型，但键只能使用字符串、数字或元组
"""
XiaoMing_dict = {"name": "小明",
                 "gender": True,
                 "height": 1.75,
                 "weight": 75.5}

# 1.取值(如果指定的 key 不存在，程序会报错)
print(XiaoMing_dict["name"])

# 2.增加/修改
# 如果 key 不存在，会新增键值对
XiaoMing_dict["age"] = 21
# 如果键值对存在，会修改相应的键值对
XiaoMing_dict["name"] = "小小明"

# 3.删除
XiaoMing_dict.pop("name")

print(XiaoMing_dict)
