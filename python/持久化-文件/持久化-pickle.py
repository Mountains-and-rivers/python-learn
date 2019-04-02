'''
    持久化 pickle
        序列化(持久化，落地)：把程序运行中的信息保存到磁盘上
        反序列化：序列化的逆过程
        pickle：python提供的序列化模块
        pickle: dump序列化
        pickle: load反序列化
    可以保存结构化数据
'''
import pickle
# 序列化
age = 19
with open(r"test01.txt", "wb") as f:
    pickle.dump(age, f)
# 反序列化
with open(r"test01.txt", "rb") as f:
    age = pickle.load(f)
    print("age=", age)


# 序列化案例
with open(r"test01.txt", "wb") as f:
    a = [12, "Nico", [11, 12]]
    pickle.dump(a, f)
with open(r"test01.txt", "rb") as f:
    a = pickle.load(f)
    print(a)
