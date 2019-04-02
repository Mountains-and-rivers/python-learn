'''
    filter函数
        过滤函数 对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
'''
def isEven(n):
    return n%2 == 0

list1 = [i for i in range(10)]
print("list1=", list1)
rst = filter(isEven, list1)
print(rst)
print([i for i in rst])
