import calendar

'''
    calendar: 获取一年的日历字符串
    参数:
        w = 每个日期之间的间隔字符数
        l = 每周所占的行数
        c = 每个月之间的间隔字符数
'''
# calendar(), prcal(): print calendar打印日历
cal = calendar.calendar(2017)
print(type(cal))
print(cal)

cal = calendar.calendar(2017, l=0, c=3)
print(type(cal))
print(cal)
print("*" *60)

# isleap()判断某年是否是闰年
print("2000年是否是闰年", calendar.isleap(2000), "2018年是否是闰年", calendar.isleap(2018))
print("*" *60)

# leapdays()获取一个年份区间里有多少个闰年
print("2000-2019的闰年数", calendar.leapdays(2000, 2019))
print("*" *60)

# month(),prmonth()获取莫个月的日历字符串
print(calendar.month(2018, 7))
print("*" *60)

# monthrange()获取某月从周几开始和当月总天数 返回元组，0-6表示周一周日
print("2018/7从开始日期和当月总天数", calendar.monthrange(2018, 7))
print(calendar.month(2017, 7))
print("*" *60)

#  monthcalendar()返回某月的一个矩阵即二级列表，没有的天数用0表示
monthcalendar = calendar.monthcalendar(2018, 7)
print(type(monthcalendar))
print("2018/7")
for mc in monthcalendar:
    for dd in mc:
        if dd<10:
            print(dd, " ", end="")
        else:
            print(dd, "", end="")
    print()
print("*" *60)


# weekday()获取某天是周几
print("2018/7/21日是周", calendar.weekday(2018, 7, 21)+1)
