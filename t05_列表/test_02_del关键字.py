"""
    使用 del 关键字删除列表元素
"""

name_list = ["张三", "李四", "王五"]

# 使用 del 关键字删除列表元素
del name_list[1]

# del 关键字 del 实质上是用来讲一个变量从内存中删除,
# 后续程序就不能使用这个变量
name = "小明"
del name
print(name)

print(name_list)
