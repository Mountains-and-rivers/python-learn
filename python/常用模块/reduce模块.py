from functools import reduce
'''
    reduce 原意是归并，缩减
    把一个可迭代对象最后归并成一个结果
    传参要求：必须有两个参数，必须返回结果
    reduce([1,2,3,4,5,6]) == f(f(f(f(f(1, 2), 3), 4), 5), 6)
'''

def myAdd(x, y):
    return x+y

rst = reduce(myAdd, [1,2,3,4,5,6])
print(rst)
