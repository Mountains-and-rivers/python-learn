import abc

'''
    抽象类
        抽象类里可以包含有抽象方法，也可以包含具体方法
        抽象类中可以有方法，也可以有属性
        抽象类不允许实列化
        抽象类必须继承才能使用，且继承的子类必须实现所有继承来的抽象方法
        若子类没有事项父类所有抽象方法，则改子类不能被实列化
        抽象类的主要作用是规范类
'''

# 声明一个类并指定当前类的元类
class Human(metaclass = abc.ABCMeta):

    # 定义抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def slep(self):
        print("slepping...")
