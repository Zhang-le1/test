# 要求：以下文本顺序并且居中对齐

poem = ["登鹳雀楼",
         "王之涣",
         "白日依山尽",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]
# 居中对齐(使用空格填充至相应宽度)
for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))

# 向左对齐(使用空格填充至相应宽度)
for poem_str in poem:
    print("|%s|" % poem_str.ljust(10, "　"))

# 向右对齐(使用空格填充至相应宽度)
for poem_str in poem:
    print("|%s|" % poem_str.rjust(10, "　"))
