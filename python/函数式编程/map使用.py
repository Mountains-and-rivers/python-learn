'''
    map原意是映射，即把集合或者列表的每一个元素进行一定的操作，生成一个新的列表或集合
'''
def mul(n):
    return n*10

l1 = [i for i in range(10)]
l2 = map(mul, l1)
for i in l2:
    print(i)
l3 = [i for i in l2]
#print("l3=", l3)
#l3 = [i for i in l2]
print("l1=", l1)
print("l2=", l2)
# 经历一次循环后使用for生成l3值变成[]
print("l3=", l3)
