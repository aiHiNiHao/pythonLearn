class Person():
    def __init__(self):
        self.name = "lijing"
        self.age = 13
    def __call__(self):
        print("我是 call 方法")
        return
    def __getattr__(self, attr):
        return print("没有{}这个属性".format(attr))

p = Person()
print(p.name)
print(p.age)
print(p.email)
print("-"*28)

from types import MethodType

class Animal():
    pass

def move(self):
    print("我在动")

a = Animal()
a.move = MethodType(move, Animal)
a.move()
print("-"*28)

class Country(type):
    def __new__(cls, name,bases,attrs):
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        attrs["name"] = "中国"
        attrs["addr"] = "Asina"
        return type.__new__(cls,name,bases,attrs)
class China(object,metaclass=Country):
    pass

c = China()
print(c.name)

print("-"*28)

def play(self):
    print("playing")
def sleep(self):
    print("sleeping")
A = type("PersonA",(object,), {"personPlay":play, "personSleep":sleep})
a = A()
a.personPlay()
a.personSleep()