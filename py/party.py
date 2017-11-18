class Classmate(object):
    def __init__(self, name=''):
        self.name = name
    def eat(self):
        print '%s is eating' % self.name
    def drink(self):
        print '%s is drinking' % self.name

class Pythoner(Classmate):
    def occupation(self):
        print("%s occupation is pythoner" % self.name)
        
class Accounting(Classmate):
    def occupation(self):
        print("%s occupation is accounting" % self.name)

class Male(Classmate):
    def drink(self):
        print '%s is drinking alcohol' % self.name
class Female(Classmate):
    def drink(self):
        print '%s is drinking juice' % self.name

class FemaleAndPythoner(Pythoner,Female):
    pass
class MaleAndPythoner(Pythoner,Male):
    pass

if __name__ == '__main__':
    sara = Pythoner('sara')
    sara.eat()
    sara.drink()

    mickel = Accounting('mickel')
    mickel.eat()
    mickel.drink()

    branda = FemaleAndPythoner('branda')
    john = MaleAndPythoner('john')
    branda.drink()
    john.drink()