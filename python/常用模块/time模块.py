'''
    时间戳
        一个时间表示，根据不同语言，可以是整数或者浮点数
        是从1970/1/1 00:00:00到现在经历的秒数
        如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
        32位操作系统能够支持到2038年
        
    UTC时间
        UTC又称世界协调时间，以英国的格林尼治天文所在地区时间作为参考，又称世界标准时间
        中国时间 UTC+8
        
    夏令时
        夏令时就是在夏天的时候将时间条块一小时，本意是督促早睡早起，成为25小时，实际还是24小时

    时间元组
        一个包含时间内容的普通元组

    时间结构:
                    
        索引    内容        属性        值
        
         0       年        tm_year     2015
         1       月        tm_mon      1-12
         2       日        tm_mday     1-31
         3       时        tm_hour     0-23
         4       分        tm_min      0-59
         5       秒        tm_sec      0-61  60表示闰秒  61保留值
         6       周几      tm_wday     0-6
         7       第几天    tm_yday     1-356
         8       夏令时    tm_isdst    0, 1, -1(表示夏令时)
         
'''
# 使用时需导入
import time
# 时间模块的属性
# timezone: 当前时区和UTC时间相差的秒数，在没有夏令时的情况下，东八区的是 -8 = -2880
# altzone: 在夏令时的情况下，获取当前时区与UTC时间相差的秒数
print("时差:", time.timezone)
print("当前夏令时时间与UTC时间相差{0}秒".format(time.altzone))
print("*" *60)

# time() 得到时间戳 返回浮点型
t = time.time()
print(type(t))
print("时间戳:", t)

# mktime() 使用时间元组获取对应的时间戳， 返回浮点型
t = time.localtime()
tt = time.mktime(t)
print(type(tt))
print("时间戳:", tt)
print("*" *60)

# 获取当前时间 得到当前时间的时间结构， 可通过点好操作符得到相应的属性元素的内容
t = time.localtime()
print(type(t))
print(t)

# asctime() 返回元组的正常字符串化后的时间格式
t = time.localtime()
tt = time.asctime(t)
print(type(tt))
print(tt)

# ctime() 获取字符串化的当前时间, asctime的简化方式
t = time.ctime()
print(type(t))
print(t)
print("*" *60)
# clock() 获取cpu时间， 3.0-3.3可用，3.6调用有问题
time.sleep(3)
print("cpu时间", time.clock())

# sleep() 是程序进入睡眠，n秒后继续
for i in range(4):
    print(i)
    time.sleep(1)
print("*" *60)

# strftime() 将时间元组转化为自定义字符串格式
t = time.localtime()
ft = time.strftime("%Y/%m/%d  %H:%M:%S", t)
print(ft)
