class Singleton():
    __instance=None
    def __init__(self):
        pass
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

a=Singleton.getInstance()
b=Singleton.getInstance()
print(a)
print(b)