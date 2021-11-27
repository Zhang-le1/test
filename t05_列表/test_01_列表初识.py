"""
    List（列表）是python 中使用最频繁的数据类型，在其他语言中通常叫做数组
    列表专门用于存储一串信息
    列表用 [] 定义，数据之间使用 ，分隔
    列表的索引从 0 开始
        索引就是数据在列表中的位置编号，索引又可以被称为下标
    注意：从列表中取值时，如果 "超出索引范围"，程序会报错;
         从列表中取索引时，如果值不在列表中，程序会报错
"""
name_list = ["ZhangSan", "LiSi", "WanWu"]

# 1.取值和取索引 index 方法
print(name_list[1])
print(name_list.index("WanWu"))

# 2.修改
name_list[1] = "李四"
print(name_list[1])

# 3.增加
# append在列表末尾增加;
# insert在指定位置增加;
# extend 在列表末尾追加其他列表内容
name_list.append("王旭奥")
name_list.insert(1, "小美美")

temp_list = ["孙悟空", "猪八戒", "沙僧"]
name_list.extend(temp_list)

# 4.删除
# remove 从列表中删除指定内容
# pop 默认删除列表中最后一个元素/删除指定索引的数据
# clear 清空整个列表
name_list.remove("WanWu")
name_list.pop()
name_list.pop(2)
name_list.clear()

print(name_list)
