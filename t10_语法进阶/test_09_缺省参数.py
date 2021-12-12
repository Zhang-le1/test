"""
    定义函数时，可以给 某个参数 指定一个默认值，具有默认值的参数就叫做缺省参数
    调用函数时，如果没有传入 缺省参数 的值，则在函数内部使用定义函数时指定的参数默认值
    函数的额缺省参数，将常见的值设置为参数的缺省值，从而简化函数的使用
"""

gl_list = [5, 3, 9]

# sort方法中，默认按照升序排序
gl_list.sort()
print(gl_list)

# 只有当降序排序时，才需要传递 reverse 参数
gl_list.sort(reverse=True)
print(gl_list)

"""
    函数的缺省参数定义
    注意：
        1、缺省参数，需要使用最常见的值作为默认值
        2、如果一个参数的值不能确定，则不应该设置默认值，具体的数值在调用函数时由外界传递
"""


def print_info(name, gender=True):
    """

    :param name: 班上同学的姓名
    :param gender: True 男生  False 女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小刚")
print_info("小明", False)
