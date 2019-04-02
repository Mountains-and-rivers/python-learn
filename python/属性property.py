class Student():
    def fset(self, name):
        self._name = name.upper()
        
    def fget(self):
        return self._name
        
    def fdel(self):
        print(self._name)
        self._name = "NoName"
        print(self._name)
        
    name = property(fget, fset, fdel,"property的使用")
    
stu = Student()
stu.name = "Nico"
stu.fdel()

