class Animal():
    def __init__(self, name=''):
        self.__name = name
    def get_name(self):
        return self.__name

    def run(self):
        print 'Animal is runing ...'
    def drink(self):
        print 'Animal is drinking water ...'

class Dog(Animal):
    def run(self):
        print '%s is runing ...' % self.get_name()
    def bark(self):
        print 'Dog %s is barking' % self.get_name()

class Cat(Animal):
    def run(self):
        print '%s is running ...' % self.get_name()
    def miaow(self):
        print 'Cat %s is miaow' % self.get_name()

if __name__ == '__main__':
    bark = Dog('wangwang')
    print bark.get_name()
    bark.run()
    bark.drink()
    bark.bark()

    miaow = Cat('miaomiao')
    miaow.run()
    miaow.miaow()