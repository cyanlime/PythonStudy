def days(year, month, day):
    leap = 0
    if (year%400==0) or (year%4==0 and year%100!=0):
        leap = 1
    if leap==0:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap==1:
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month>12) or (month>=1 and month<=12 and days[month-1]<day) or (leap==0 and day==29):
        return 'The day not exist.'

    daymon = 0
    for mon in range(0, month-1):
        daymon += days[mon]
    daymon+=day
    return year, month, day, daymon

if __name__ == "__main__":
    days = days(2016,1,7)
    if type(days)==tuple:
        year, month, day, daymon = days
        print '%s-%s-%s is the %s day of the year' % (year, month, day, daymon)
    else:
        print days