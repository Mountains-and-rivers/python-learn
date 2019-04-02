import random
'''
    Random
        随机数
        所有随机数模块都是伪随机
'''
# random() 获取0-1之间的随机小数
print("随机小数", random.random())
print("随机0-100", random.random()*100)

# choice(序列) 随机返回序列对应的值
lst = ["h"+str(i) for i in range(10)]
print("list = ", lst)
print("list随机", random.choice(lst))

# shuffle() 随机打乱列表中的值
lst = ["h"+str(i) for i in range(10)]
print("list = ", lst)
random.shuffle(lst) # 打乱元列表中值
print("list打乱", lst)

# randint() 随机返回一个整数
print("随机0-100", random.randint(0, 100))
