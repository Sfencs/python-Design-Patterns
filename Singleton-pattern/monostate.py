class Monostate():
    _shared_state={}
    def __init__(self):
        self.x=1
        self.__dict__=self._shared_state

a=Monostate()
b=Monostate()
b.x=5
print(a)#<__main__.Monostate object at 0x000001C267714B38>
print(b)#<__main__.Monostate object at 0x000001C267714B00>
print(a.x)#5
a.c=4
print(b.c)#4