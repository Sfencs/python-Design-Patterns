class MetaSingleton(type):
    __instance={}
    def __call__(self, *args, **kwargs):
        if self not in MetaSingleton.__instance:
            MetaSingleton.__instance[self] = super(MetaSingleton,self).__call__()
        return MetaSingleton.__instance[self]

class Singleton(metaclass=MetaSingleton):
    def __init__(self):
        pass

a=Singleton()
b=Singleton()
print(a)
print(b)