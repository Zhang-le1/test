"""
    len（） 计算容器中元素的个数
    del（） 删除变量
    max（） 返回容器中元素最大值，如果是字典，只针对key比较
    min（） 返回容器中元素最小值，如果只字典，只针对key比较
    < 或 >  可以对字符串，列表，元组，进行大小比较，字段不能比较大小
"""
test_list = [1, 2, 4, 9, 0, 7, 5]

print(len(test_list))
print(max(test_list))
print(min(test_list))

test_dict = {"a": "z", "b": "y", "c": "x"}
print(max(test_dict))
print(min(test_dict))
