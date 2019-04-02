class Person():
    def __init__(self, name="NoName", age=18):
        print("Person init ...")
        self.name = name
        self.age = age

    def say(self):
        print(self.name, "-->", self.age)

def sayHello():
    print("hello, welcome to my sapce!!")

# 判断此文件是否作为主线程执行
# 建议一直最为判断程序的入口, 可以有效地避免模块导入时被动地执行一次
if __name__ == '__main__':
    print("module Person")
