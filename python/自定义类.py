from types import MethodType # 从types里导入MethodType

'''
    自定义类
        类其实是一个类定义和各种方法的自由组合
        可以定义类和函数然后通过类直接赋值
        可以借助MethodType实现
        借助于type实现
        利用元类 MetaClass
            元类是类
            beiyonglai创造别的类
'''

class A():
    pass

# 定义在类外部的方法，可作为变量使用
def say(self):
    print("saying...")
# 直接调用
say(0)

'''
    将函数名作为变量赋值给类A中的属性say 即将方法say(self)组装到类A
    组装后的类A:
    
    class A():
        def say(self):
            print("saying...")
'''
# 将方法组装到类A中
A.say = say
a = A()
a.say()

print("-" *60)
print()





# 函数名可以当变量使用 即将方法的内存地址赋值给变量
def sayHello(name):
    print(name,"sayHello...")
    
sayHello("Nico")
manSay = sayHello
manSay("man")

print("-" *60)
print()






# 将方法组装到类A的实例中
def haha(self):
    print("组装到实列...")

aa = A()
print(aa.__dict__)

# 明确告知系统haha是一个方法，将haha放入dao实列aa中
aa.haha = MethodType(haha, A)
aa.haha()
print(aa.__dict__)
print(A.__dict__)

print("-" *60)
print()






# 利用type造一个类

def say(self):
    print("saying...")

def talk(self):
    print("talking")

# 用type创建一个类
C = type("TypeCreateA", (object, ), {"class_say":say, "class_talk":talk})

print(C.__dict__)
c = C()
c.class_say()
c.class_talk()

print("-" *60)
print()




# 元类写法固定，必须继承type
# 元类一般命名以MetaClass结尾
class TulingMetaClass(type):
    # 注意写法
    def __new__(cls, name, bases, attrs):
        print("元类...")
        attrs['id'] = "00001"
        attrs['addr'] = "北京海淀区公主坟西翠路12号"
        return type.__new__(cls, name, bases, attrs)

# 元类定义完成即可使用，注意写法
class Teacher(object, metaclass = TulingMetaClass):
    pass
teacher = Teacher()
print(teacher.id)
print(Teacher.__dict__)
