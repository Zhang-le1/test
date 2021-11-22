"""
    1、定义布尔型变量 has_ticket 表示是否有车票
    2、定义整型变量 knife_length 表示刀的长度，单位：厘米
    3、安检时，需要检查刀的长度，判断是否超过20厘米，
       如果超过20厘米，提示刀的长度，不允许上车
       如果不超过20厘米，安检通过
    4、如果没有车票，不允许进门
"""
has_ticket = True
knife_length = 21
if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length <= 20:
        print("安检通过")
    else:
        print("您携带的道具有%d厘米，不允许上车" % knife_length)

else:
    print("请先买票！！！")
