from abc import ABCMeta,abstractmethod

class Coke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self):
        pass

class Coca(Coke):
    def drink(self):
        print('drink Coca-Cola')

class Pepsi(Coke):
    def drink(self):
        print('drink Pepsi-Cola')

class Fast_food_restaurant():
    def make_coke(self ,name):
        return eval(name)()

KCD=Fast_food_restaurant()
coke=KCD.make_coke('Coca')
coke.drink()#drink Coca-Cola