"""
    Tuple(元组)与列表类似，不同之处在于元组的 元素不能修改
        元组表示多个元素组成的序列
        元组在python开发中，有特定的应用场景
    用于存储一串信息，数据之间使用 ，分隔
    元组用（ ）定义
    元组的索引从 0 开始
        索引就是数据在元组中的位置编号
"""
info_tuple = ("zhang", 18, 1.75)
print(info_tuple[1])
print(type(info_tuple))

# 定义空元组
empty_tuple = ()
print(type(empty_tuple))

# 元组中只有一个元素时，在元素后需要添加逗号
# 如果不加逗号，会被识别为 int 类型
single_tuple = (5, )
