'''
    类的魔术方法，即在特定条件下自动触发
    
    __str__ 与 __repr__ 的区别:
    __str__直接输出对象结果为对象的内存地址

    __repr__直接输出对象或者通过print打印都按__repr__方法中定义的格式进行显示

    __getattr__ 和 __setattr__方法中不能直接进行属性的赋值，否则进入死循环
'''
class Person():
    name = "noName"
    # 初始化
    def __init__(self):
        print("init...",self.name)
        self.name = "Nico"
        
    # 对象当做函数使用时调用
    def __call__(self):
        print("call...")
        
    # 对象当作字符串使用时调用
    def __str__(self):
        return "str..."
    
    # 对象当作字符串使用时调用
    def __repr__(self):
        return "repr..."

    # 所访问的属性不存在时调用 person.age <==> person-->self, age-->name
    def __getattr__(self, name):
        print("getattr... 不存在属性-->", name)
        
    # 拦截所有属性的赋值
    def __setattr__(self, name, val):
        if hasattr(self, name):
            print("setattr... 存在",name)
            print("setattr... 设置属性:", name, val)
        else:
            print("setattr... 不存在")
        
            '''
            一直递归，进入死循环
            self.name = val
            为避免进入死循环，统一规定调用父类魔法函数

            '''
            # 创建属性并赋值, 不过此属性并不会真的存在即假赋值
            super().__setattr__(name, val)
    
    def say(self):
        print("*" *10)

person = Person()
person()
print(person)
# 因为不存在Person.age属性，且此处又有print，所以结果会多出一个None
person.age
person.addr = "四川成都"
person.say()
