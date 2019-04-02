'''
    datetime 提供日期和时间的运算和表示
    datetime常见属性
        datetime.date 一个理想和日期，提供year，month，day属性
'''
import datetime

# datetime.date 提供一个居于year, month, day等内容的日期
dt = datetime.date(2018, 8, 22)
print(dt)
print(dt.year)

# datetime.time 提供一个理想和的时间，居于hour，minute, sec, microsec等内容
print(datetime.time(22, 34, 44))

# datetime.datetime 提供日期和时间的组合
print(datetime.datetime(2018, 8, 22, 10, 21, 39))

print("*" *60)






# datetime.timedelta 提供一个时间差，时间长度

from datetime import datetime, timedelta
t1 = datetime.now()
print(t1)
# td表示以小时的时间长度
td = timedelta(hours=1)
print((t1+td).strftime("%Y/%m/%d  %H:%M:%S"))

print("*" *60)





#datetime.datetime
    #常用类方法 today() now() utcnoew() fromtimestamp()从时间戳中返回本地时间

import time
from datetime import datetime

dt = datetime(2018, 8, 22)
print(dt.today())
print(dt.fromtimestamp(time.time()))

print("*" *60)




# timeit 时间测量工具

import timeit
# 比较生成列表的两种方法
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

# 测量代码c执行100000次的运行时间
t1 = timeit.timeit(stmt = c, number = 100000)
# 利用timeit调用代码，执行100000次， 查看运行时间
t2 = timeit.timeit(stmt = "[i for i in range(1000)]", number = 100000)

print("t1", t1)
print("t2", t2)
# 执行函数 timeit.timeit(stmt = function_name)或者上一个方法
