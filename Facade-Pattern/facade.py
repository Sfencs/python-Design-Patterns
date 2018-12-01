class Client():
    def order(self):
        Waiter().make_set_meal1()

class Waiter():
    def make_set_meal_1(self):
        Coke().make()
        Hamburger().make()
        French_fries().make()

class Coke():
    def make(self):
        print('making coke')

class Hamburger():
    def make(self):
        print('making hamburger')

class French_fries():
    def make(self):
        print('making french fries')

you=Client()
you.order()
'''

making coke
making hamburger
making french fries

'''