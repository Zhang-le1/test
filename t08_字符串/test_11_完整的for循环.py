"""
    for 变量 in 集合：
        循环体代码
    else：
        for循环语句完整全部执行完毕后，才会执行else语句
        如果for循环通过 break 退出循环，不会执行else语句
"""

for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    print("会执行吗？")

print("循环结束")
