from abc import abstractmethod
from abc import ABCMeta

class abstracta(metaclass=ABCMeta):
    @abstractmethod
    def funcionabstracta(self):
        pass

class nueva(abstracta):
    pass

x = nueva()
x.funcionabstracta()