"""
    缺省参数注意事项：
    1、必须保证带有默认值的缺省参数在参数列表的末尾
    2、调用带有多个缺省参数的函数时，需要指定参数名
"""


def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生  False 女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s]%s 是 %s" % (title, name, gender_text))


print_info("小刚")
print_info("小明", gender=False)
print_info("老张", title="总裁", gender=True)
