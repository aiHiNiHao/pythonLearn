import abc

class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractclassmethod
    def spake(cls):
        pass

    @abc.abstractstaticmethod
    def grow():
        pass