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

class Sfencs(Coke):
    def drink(self):
        print('drink Sfencs-Cola')

class Fast_food_restaurant(metaclass=ABCMeta):
    @abstractmethod
    def make_coke(self):
        pass

class Coca_produce(Fast_food_restaurant):
    def make_coke(self):
        return Coca()

class Pepsi_produce(Fast_food_restaurant):
    def make_coke(self):
        return Pepsi()

class Sfencs_produce(Fast_food_restaurant):
    def make_coke(self):
        return Sfencs()

KCD=Sfencs_produce()
coke=KCD.make_coke()
coke.drink()#drink Sfencs-Cola