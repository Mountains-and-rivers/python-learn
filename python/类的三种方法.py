'''
类和对象的三种方法
    实列方法
        需要实列化对象才能进行调用
    静态方法
        不需要进行实列化，通过类直接访问
    类方法
        不需要实列化
'''

class Person():
    # 实列方法 可以传类的属性和方法
    def eat(self):
        print(self)
        print("eating...")

    # 类方法 类方法的第一个参数一般命名为cls，区别于self 不能传实例的属性和方法
    @classmethod
    def play(cls):
        print(cls)
        print("playing...")

    # 静态方法 不需要用第一个参数表示自身或者类 方法体中不能使用类或实例的任何属性和方法
    @staticmethod
    def say():
        print("saying...")

person = Person()
person.eat()
print()

person.play()
Person.play
print()

person.say()
Person.say()
