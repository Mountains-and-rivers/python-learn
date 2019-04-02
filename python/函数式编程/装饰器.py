'''
   在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上装饰器就是一个返回函数的高阶函数
   装饰器使用：使用@语法，即在每次要扩张到函数定义前使用 @+函数名
   装饰器的好处是一但定义，则可以装饰任意函数
'''
import time
# 对hello函数进行功能扩展，每次执行hello前打印当前时间
# 高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time:", time.ctime())
        return f(*args, **kwargs)
    return wrapper
# 上面定义了装饰器， 使用的时候需要使用@，此符号是python的语法糖
@printTime
def hello():
    print("hello")

hello()

#手动执行下装饰器
print("手动执行下装饰器")
def hello3():
    print("手动执行...")

hello3 = printTime(hello3)
hello3()
