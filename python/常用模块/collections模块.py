'''
    collections模块
        - tuple类型
        - 是一个可命名的tuple
'''
import collections
# namedtuple
# 定义一个点
Point = collections.namedtuple("Point", ['x', 'y'])
p = Point(11, 22)
print(p.x)
print(p[1])
print("-" *60)

# 定义一个椭圆
Circle = collections.namedtuple("Cicle", ['x', 'y', 'r'])
c = Circle(100, 150, 50)
print(c)
# 检测c是否是tuple的子类
print(isinstance(c, tuple))
print("-" *60)
print()

# deque 比较方便的解决了频繁删除插入带来的效率问题
q = collections.deque(['a', 'b', 'c'])
print(q)
q.append('d')
print(q)
# 从前面插入
q.appendleft('000')
print(q)
print("-" *60)
print()

# defaultdict 当直接读取dict不存在的属性时，返回默认值
d1 = {"one":1, "two":2, "three":3}
print(d1["one"])
# print(d1["43"]) 报错
print("--")
func = lambda: "0"
d2 = collections.defaultdict(func)
d2["one"] = 1
d2["two"] = 2
print(d2["one"])
print(d2["fs"])
print("-" *60)
print()

'''
    Counter 统计可迭代数据里相同数据出现的次数
'''
c = collections.Counter("jklfahsl;gjkh;salkfg;as")
cc = collections.Counter(("Love", "I", "Love", "Love", "You", "Love",))
print(c)
print(cc)
