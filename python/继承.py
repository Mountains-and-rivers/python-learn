#单继承
class A():
    def __init__(self, name):
        print("A-->", name)

class B(A):
    def __init__(self, name):
        print("B-->", name)
    def say():
        print("say...")

class C(B):
    
    def __init__(self, name):
        print("C-->", name)
        super(C, self).__init__(name)
        B.__init__(self, name)
        print("C")

c = C("Nico")
c.__class__.say()

print("*" *20)

#多继承
class Fish():
    def __init__(self, name):
        print("fish-->", name)
    def swim(self):
        print("fish--> swimming")
        
class Bird():
    def __init__(self, name):
        print("bird--> ", name)
    def fly(self):
        print("bird--> flying")
        
class Person():
    def __init__(self, name):
        print("person-->", name)

class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        print("superMan-->", name)

superMan = SuperMan("Nico")
superMan.swim()
superMan.fly()
print(SuperMan.__mro__)
print(SuperMan.__dict__)

print("*" *20)

#MiXin
class Human():
    name = "Nico"
    age = 21
    def sleep(self):
        print("slepping...")
class Teacher():
    def work(self):
        print("teacher--> working")

class Student():
    def study(self):
        print("sttudent--> study")

class Tutor(Human, Teacher, Student):#助教：既是学生又是老师
    pass

tutor = Tutor()
tutor.work()
tutor.study()
print(Tutor.__mro__)
print(Tutor.__dict__)
print(issubclass(Tutor,Teacher))
