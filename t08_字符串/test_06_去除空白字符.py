poem = ["\t\n登鹳雀楼",
         "王之涣",
         "白日依山尽\t\n",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]

for poem_str in poem:
    # 先使用 strip 方法去除字符串中的空白字符
    # 再使用 center 方法是文本居中
    print("|%s|" % poem_str.strip().center(10, "　"))
