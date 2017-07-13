import random
class Person():
    def __init__(self, name=''):
        self.name = name
        self.lifevalue = 5000
    def speak(self):
        self.word=random.choice(["Hey, girl.", "I miss you.", "I like you.", "Good guys.", "My god."])
    def fight(self):
        self.lifevalue-=random.randint(10,200)

if __name__ == "__main__":
    sara = Person('sara')
    micheal = Person('micheal')
    while micheal.lifevalue>0 or sara.lifevalue>0:
        sara.speak()
        micheal.speak()
        print 'Micheal\'s word is %s, sara\'s word is %s' % (micheal.word, sara.word)
        sara.fight()
        micheal.fight()
        print 'Micheal\'s lifevalue is %s, sara\'s lifevalue is %s' % (micheal.lifevalue, sara.lifevalue)

    if micheal.lifevalue==0 and sara.lifevalue>0:
        print 'Game over. Sara\'s life value is %s, sara wins' % sara.lifevalue
    if sara.lifevalue==0 and micheal.lifevalue>0:
        print 'Micheal\'s life value is %s, sara wins' % micheal.lifevalue
    if micheal.lifevalue==0 and sara.lifevalue==0:
        print 'Micheal and Sara died.'