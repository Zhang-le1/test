XiaoMing_dict = {"name": "小明",
                 "gender": True,
                 "height": 1.75,
                 "weight": 75.5}

# 1.统计键值对的数量
print(len(XiaoMing_dict))

# 2.合并字典
# 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
temp_dict = {"age": 18,
             "gender": False}

XiaoMing_dict.update(temp_dict)

# 3.清空字典
XiaoMing_dict.clear()

print(XiaoMing_dict)
