"""

"""
__all__ = []
# Helper functions
def makeBreakfast():
    return Breakfast()
def makeLunch():
    return Lunch()
def makeDinner():
    return Dinner()

class SensitiveArtistException(Exception):
    pass
class AngreyChefException(SensitiveArtistException):
    pass
class Meal:
    def __init__(self, food='omelet', drink='coffee'):
        self.name = 'generic meal'
        self.food = food
        self.drink = drink
    def printIt(self, prefix=''):
        print (prefix, 'A fine', self.name, 'with', self.food, 'and', self.drink)
    def setFood(self, food='omelet'):
        self.food = food
    def setDrink(self, drink='coffee'):
        self.drink = drink
    def setName(self, name='')
        self.name = Name
class Breakfast(Meal)：
    def __init__(self):
        Meal.__init__(self, 'omelet', 'coffee')
        self.setName('breakfast')
class Lunch(Meal):
    def __init__(self):
        Meal.__init__(self, 'sandwith', 'gin and tonic')
        self.setName('midday meal')
    def setFood(self, food='sandwich'):
        if food!='sandwich' and food!='omelet':
            raise AngreyChefException
        Meal.setFood(self，food)
class Dinner(Meal):
    def __init__(self):
        Meal.__init__(self, 'steak', 'merlot')
        self.setName('dinner')
    def printIt(self, prefix=''):
        print(prefix, 'A gourment', self.name, 'with', self.food, 'and', self.drink)

def test():
    print("Module meal test")
    print('Testing Meal class')
    m = Meal()
    m.printIt("\t")

    m = Meal('green eggs and ham', 'tea')
    m.printIt("\t")

    b=Bre
    