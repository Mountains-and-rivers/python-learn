import os
'''
    zip 把两个可迭代的内容生成一个可迭代的tuple元素类型组成的内容
'''
# zip案例1
print("zip案例1")
list1 = [1,2,3,4]
list2 = [11,22,33,44]
z = zip(list1, list2)
print(z)
for i in z:
    print(i)
print("#" *60)
# zip案例2
print("zip案例2")
list1 = ["zz", "md", "yyt"]
list2 = [80, 88, 90]
z = zip(list1, list2)
for i in z:
    print(i)
print("#" *60)

'''
    enumerate
        跟zip相像 对可迭代的对象里的每一元素配上一个索引，然后索引和内容构成tuple类型
'''
# enumerate案例
print("enumerate案例")
list1 = [11,22,33,44,55]
em = enumerate(list1)
for i in em:
    print(i)
em = enumerate(list1, start=100)
# 指定索引开始值
for i in em:
    print(i)
print("#" *60, os.linesep*3)


