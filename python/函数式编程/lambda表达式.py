'''
    lambda 表达式的用法
        以lambda开头
        紧跟一定的参数(如果有的话)
        参数后用冒号和表达式主题分开
        只是一个表达式，没有return
'''

# 计算一个数字的100倍 因为是一个表达式所以没有return
stm = lambda a: 100*a
print(stm(11))

# 多参数lambda表达式
st = lambda a,b,c: a + b*10 + c*100
print(st(1,2,3))
