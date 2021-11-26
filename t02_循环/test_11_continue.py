# continue 某一条件满足时，不执行后续重复的代码（跳过这一次循环，继续执行后续循环语句）

i = 0
while i < 10:
    if i == 3:
        # 注意：在循环中，如果使用continue这个关键字
        # 在使用之前，需要确认循环计数是否修改，否则可能导致死循环
        i = i + 1
        continue
    print(i)
    i += 1
print("over")
