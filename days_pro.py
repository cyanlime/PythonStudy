def days(startdate, enddate):
    start_year = startdate[0]
    start_month = startdate[1]
    start_day = startdate[2]

    end_year = enddate[0]
    end_month = enddate[1]
    end_day = enddate[2]

    start_year_leap=0
    end_year_leap=0
    if (start_year%400==0) or (start_year%4==0 and start_year%100!=0):
        start_year_leap = 1
    if (end_year%400==0) or (end_year%4==0 and end_year%100!=0):
        end_year_leap = 1

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if end_month>12 or end_month<1 or start_month>12 or end_month<1:
        return "month not exist"
    if (start_year_leap==0 and days[start_month-1]<start_day) or (end_year_leap==0 and days[end_month-1]<end_day)\
        or (start_year_leap==1 and start_month==2 and start_day>29) or \
        (end_year_leap==1 and end_month==2 and end_day>29):
        return "day not exist"

    if end_year>start_year:
        rest_day = days[start_month-1]-start_day
        if rest_day==-1:
            rest_day=0
        for month in range(start_month, 12):
            rest_day+=days[month]
        for year in range(start_year+1, end_year):
            if (year%400==0) or (year%4==0 and year%100!=0):
                rest_day+=366
            else:
                rest_day+=365
        if end_month>=2:
            for month in range(0, end_month-1):
                rest_day+=days[month]
        rest_day+=end_day

        if start_year_leap==1 and start_month<=2 and start_day!=29:
            rest_day+=1
        if end_year_leap==1 and end_month>=3:
            rest_day+=1
        return startdate, enddate, rest_day

    if end_year==start_year and end_month>start_month:
        rest_day = days[start_month-1]-start_day
        if rest_day==-1:
            rest_day=0
        for month in range(start_month, end_month-1):
            rest_day+=days[month]
        rest_day+=end_day
        if start_year_leap==1 and start_month<=2 and start_day!=29 and end_month>=3:
            rest_day+=1
        return startdate, enddate, rest_day

    if end_year==start_year and end_month==start_month:
        rest_day = end_day-start_day
        return startdate, enddate, rest_day

if __name__ == "__main__":
    days = days((1993,11,2), (1994,1,2))  
    if type(days)==tuple:
        startdate, enddate, rest_day = days
        print '%s days between %s and %s' % (rest_day, startdate, enddate)
    else:
        print days