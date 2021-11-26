"""
    break 和 continue 是专门在循环中使用的关键字
    break 某一条件满足时，退出循环，不再执行后续重复的代码(退出整个循环)
    continue 某一条件满足时，不执行后续重复的代码
    （跳过这一次循环，继续执行后续循环语句）
    break和continue 只针对当前所在循环有效
"""
i = 0

while i < 10:
    if i == 3:
        break

    print(i)

    i += 1
print("over")
