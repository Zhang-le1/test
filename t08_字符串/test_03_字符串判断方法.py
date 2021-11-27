# 1、判断空白字符
space_str = "  \t\n\r"

print(space_str.isspace())

# 2、判断字符串中是否只包含数字
# 以下三种方法都不能判断小数
num_str = "1"

print(num_str)
print(num_str.isdecimal())

# 可以判断 unicode 字符串 （1） \u00b2
print(num_str.isdigit())

# 可以判断 unicode 字符串
# 可以判断中文数字
print(num_str.isnumeric())
