"""
    字符串的定义
    1、字符串就是一串字符，是编程语言中表示文本的数据类型
    2、在 python 中可以使用 一对双引号 或 一对单引号 定义一个字符串
        一般使用双引号定义字符串
        如果字符串内有双引号，可使用单引号定义字符串
    3、可以使用 索引 获取一个字符串中指定位置的字符，索引计数从0开始
    4、也可以使用 for 循环遍历字符串中每一个字符
"""
# 一般使用双引号定义字符串
str1 = "hello python"
# 如果字符串内有双引号，可使用单引号定义字符串
str2 = '我的外号叫"大西瓜"'
print(str1)
print(str2)

# 可以使用 索引 获取一个字符串中指定位置的字符，索引计数从0开始
print(str2[0])

# 也可以使用 for 循环遍历字符串中每一个字符
for char in str2:
    print(char)
