"""
    计算0~100之间所有偶数的和
"""
i = 0
s = 0
while i <= 100:
    if i % 2 == 0:
        s = s + i
        print(i)
    i += 1
print(s)
