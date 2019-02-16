class Person():
    name = "xiaoli"
    arg = 25

    def speak(self):
        print(self.name, ":" , self.arg)
        return

Person.speak(Person)

xiaoli = Person()
xiaoli.arg = 24
xiaoli.name = "zxl"
xiaoli.speak()

print("_"*20)

# 构造函数
class Dog():
    age = 1
    name = "xiaoqiang"

    def __init__(self):
        self.age = 2
        self.name = "wangcai"
        return
    def show(self):
        print("age = {0}".format(self.age))
        print("name = {0}".format(self.name))
        return

Dog.show(Dog)

dog = Dog()
dog.show()

print("* "*30)

class Student():
    name = "xiaoli"
    __age = 25

    def __init__(self):
        self.name = "lijing"
        self.__age = "26"
        return

    def speak(self):
        print("name = {0}".format(self.name))
        print("age = {0}".format(self.__age))

Student.speak(Student)

student = Student()
student.speak()

print("* +"*30)
student.name = "zxl"
student.__age = 18
student._Student__age = 20
student.speak()

print(student.__dict__)

print("*-+"*30)

class A():

    name = "ljing"
    age = 100

    def say(self):
        print("name = {0}".format(self.name))
        print("age = {0}".format(self.age))
        return

    def sayAgain():
        print("name again= {0}".format(__class__.name))
        print("age again= {0}".format(__class__.age))
        return

a = A()
a.say()

A.sayAgain()