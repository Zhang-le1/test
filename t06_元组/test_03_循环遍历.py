
info_tuple = ("ZhangSan", 18, 1.75)

# 使用迭代遍历元组
for my_info in info_tuple:
    # 使用格式字符串拼接 my_info 这个变量不方便
    # 因为元组中通常保存的数据类型是不同的
    print(my_info)

"""
    元组的应用场景：
    1、函数的参数和返回值，一个函数可以接受任意多个参数，
    或者一次返回多个数据
    2、格式字符串，格式化字符串后面的（）本质上就是一个元组
    3、让列表不可以被修改，以保护数据安全
"""
# 格式化字符串
print("%s 年龄是 %d,身高是%.2f" % info_tuple)
info_str = "%s 年龄是 %d,身高是%.2f" % info_tuple
print(info_str)
