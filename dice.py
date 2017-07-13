import random
def dice(name, times):
    sum = 0
    print 'Dice %s points:' % name
    for time in range(0, times):
        num = random.randint(1, 6)
        print num
        sum+=num
    return sum

if __name__ == '__main__':
    print 'Dicing start.'
    points_A = dice("A", 3)
    points_B = dice("B", 3)
    print 'Dicing end.'
    if points_A>points_B:
        print 'Sum of dice points A is %s, B is %s. A win' % (points_A,points_B)
    elif points_A<points_B:
        print 'Sum of dice points A is %s, B is %s. B win' % (points_A,points_B)
    else:
        print 'Sum of dice points A is %s, B is %s. Again' % (points_A,points_B)
