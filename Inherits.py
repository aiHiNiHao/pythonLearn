class Person():
    firstName = "李"
    # __age = 50  # 只能自己访问，子类不能访问
    _age = 50  # 受保护的， protect
    _money = 10000

    def __init__(self):
        print("我姓李")
        return

    def speak(self):
        print("我叫李, 今年{}岁了，我有{}钱".format(self._age, self._money))

    def _life(self):
        self.__work()
        self._sleep()

    def __work(self):
        print("我会挣钱")

    def _sleep(self):
        print("我会睡觉")


class Student(Person):
    pass

    def speak(self):
        super().speak()
        print("我叫李静, 今年{}岁了，我爸爸给我{}钱".format(self._age, self._money))


person = Person()
person.speak()
person._life()

print("_"*20)

student = Student()
student._age = 18
student.speak()
student._sleep()
