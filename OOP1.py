# 访问私有变量
# 类里面的属性不是
class Person():
    arg = 1
    __name = "xiaoli"

    def __init__(self, name):
        self.__name = name
        return
    def getName(self):
        return self.__name


# p = Person("lijing")
# print(p.__getattribute__("_Person__name"))
# print(p.getName())
#
# print(p.__dict__)#在没有给p的arg属性赋值钱，p.__dict__里没有arg属性
# print(p.arg)
# p.arg = 3
# print(p.__dict__)
class Animal():
    pass

class Fish(Animal):
    __skill = "游泳"

    def getSkill(self):
        return self.__skill

class Bird(Animal):
    __skill = "飞"

    def getSkill(self):
        return self.__skill

class Duck(Bird, Fish):
    pass

duck = Duck()
print()
print(Duck.__bases__)
print(duck.getSkill())#多继承是，如果有多个父类都有同一个方法， 优先执行第一个父类的方法