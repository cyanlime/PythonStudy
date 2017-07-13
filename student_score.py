class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print '%s score is %s' % (self.__name, self.__score)
    
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score>=90:
            print "A"
        elif self.__score>=70 and self.__score<=90:
            print 'B'
        elif self.__score>=60 and self.__score<=70:
            print 'C'
        else:
            print 'D'

if __name__ == "__main__":
    sara = Student('sara', 60)
    sara.print_score()
    sara.get_grade()

    print sara.get_name()
    print sara.get_score()
    sara.set_score(70)
    print sara.get_score()
