#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3

def md5_Encode(str):
        import hashlib
        m = hashlib.md5(str.encode(encoding='utf-8'))
        return m.hexdigest()


in_str = input("请输入要加密的字符串：")

last_str = "ce2f13620eb5d179dwd"


d1 = md5_Encode(in_str)
sec_str = d1.upper()+last_str

d2 = md5_Encode(sec_str)
print(d2.upper())

