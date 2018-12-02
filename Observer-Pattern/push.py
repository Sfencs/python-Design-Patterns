from abc import ABCMeta,abstractmethod


class NewsPublisher:           #subject
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self,subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update(self.__latestNews)

    def addNews(self,news):
        self.__latestNews = news

    def getNews(self):
        return 'Got News:'+self.__latestNews


class Subscriber(metaclass=ABCMeta):       #Observer

    @abstractmethod
    def update(self):
        pass


class ConcreteSubscriber1:           #ConcreteObserver
    def __init__(self,publisher):
        self.publisher=publisher
        self.publisher.attach(self)

    def update(self,news):
        print(type(self).__name__,news)


class ConcreteSubscriber2:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self,news):
        print(type(self).__name__, news)


news_publisher = NewsPublisher()
for Subscribers in [ConcreteSubscriber1,ConcreteSubscriber2]:  #创建观察者对象
    Subscribers(news_publisher)

news_publisher.addNews('HELLO WORLD')
news_publisher.notifySubscribers()
news_publisher.detach()
news_publisher.addNews('SECOND NEWS')
news_publisher.notifySubscribers()
'''
ConcreteSubscriber1 HELLO WORLD
ConcreteSubscriber2 HELLO WORLD
ConcreteSubscriber1 SECOND NEWS
'''