"""
    计算0~100之间所有数字的累计求和结果
"""
i = 0
s = 0
while i <= 100:
    s = s + i
    i = i + 1
print(s)
