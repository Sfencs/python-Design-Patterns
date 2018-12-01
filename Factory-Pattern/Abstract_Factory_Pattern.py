from abc import ABCMeta,abstractmethod

class Ice_coke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self):
        pass

class Ordinary_coke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self):
        pass

class Coca_ice(Ice_coke):
    def drink(self):
        print('drink  Coca-ice-Cola')

class Pepsi_ice(Ice_coke):
    def drink(self):
        print('drink Pepsi-ice-Cola')

class Coca_ordinary(Ordinary_coke):
    def drink(self):
        print('drink Coca-ordinary-Cola')

class Pepsi_ordinary(Ordinary_coke):
    def drink(self):
        print('drink Pepsi-ordinary-Cola')

class Fast_food_restaurant(metaclass=ABCMeta):
    @abstractmethod
    def make_ice_coke(self):
        pass

    @abstractmethod
    def make_ordinary_coke(self):
        pass

class Coca_produce(Fast_food_restaurant):
    def make_ice_coke(self):
        return Coca_ice()
    def make_ordinary_coke(self):
        return Coca_ordinary()

class Pepsi_produce(Fast_food_restaurant):
    def make_ice_coke(self):
        return Pepsi_ice()
    def make_ordinary_coke(self):
        return Pepsi_ordinary()

KCD=Coca_produce()
coke=KCD.make_ice_coke()
coke.drink()#drink  Coca-ice-Cola