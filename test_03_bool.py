"""
练习三：定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工
       如果不是提示不允许入内
"""
# 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用 not
# 另外，如果需要拼接复杂的逻辑运算条件时，同样也有可能使用到 not
is_employee = False
if not is_employee:
    print("非本公司元工，禁止入内")
