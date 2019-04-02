'''
    模块使用
        直接导入:
            若加入模块名称直接以数字开头
                借助于importlib包实现导入以数字开头的模块 import importlib
                将导入的模块赋值给变量，然后需要使用模块时则直接使用这个变量
                    name = improtlib.import_module("module_name")
    语法
        import module_name 导入模块， 使用时需要加前缀
        import module_name as name 导入模块时起一个别名，使用时用别名
        modeule_name.function_name 使用模块中的方法
        module_name.class_name 使用模块中的类
        from module import function_name, class_name 有选择地导入模块中的内容,使用时无前缀
        from module_name import * 导入模块中所有, 使用时不需要前缀
'''
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
