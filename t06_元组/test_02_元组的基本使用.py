info_tuple = ("ZhangSan", 18, 1.75, "ZhangSan")
print(info_tuple)
# 1.取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index(18))

# 2.统计计数
# 统计某元素在元组中出现的次数
print(info_tuple.count("ZhangSan"))
# 统计元组中元素的个数
print(len(info_tuple))
