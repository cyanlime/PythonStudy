def days(startdate, enddate):
    start_year = startdate[0]
    start_month = startdate[1]
    start_day = startdate[2]

    end_year = enddate[0]
    end_month = enddate[1]
    end_day = enddate[2]

    # leap = 0
    # for year in [start_year, end_year]:
    #     if (year%400==0) or (year%4==0 and year%100!=0):
    #         leap = 1

    start_year_leap=0
    end_year_leap=0
    if (start_year%400==0) or (start_year%4==0 and start_year%100!=0):
        start_year_leap = 1
    if (end_year%400==0) or (end_year%4==0 and end_year%100!=0):
        end_year_leap = 1
    
    if start_year_leap==0 and end_year_leap==0:
        start_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        end_days = start_days
    if start_year_leap==1 and end_year_leap==1:
        start_days = [31, 29 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        end_days = start_days
    if start_year_leap==0 and end_year_leap==1:
        start_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        end_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if start_year_leap==1 and end_year_leap==0:
        start_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        end_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    

    if end_year>start_year:
        rest_day = start_days[start_month-1]-start_day
        for month in range(start_month, 12):
            rest_day+=start_days[month]
        for year in range(start_year+1, end_year):
            if (year%400==0) or (year%4==0 and year%100!=0):
                rest_day+=366
            else:
                rest_day+=365
        if end_month>=2:
            for month in range(0, end_month-1):
                rest_day+=end_days[month]
        rest_day+=end_day
        return startdate, enddate, rest_day

    if end_year==start_year and end_month>start_month:
        rest_day = start_days[start_month-1]-start_day
        for month in range(start_month, end_month-1):
            rest_day+=start_days[month]
        rest_day+=end_day
        return startdate, enddate, rest_day

    if end_year==start_year and end_month==start_month:
        rest_day = end_day-start_day
        return startdate, enddate, rest_day


if __name__ == "__main__":
    startdate, enddate, rest_day = days((1994,1,6), (2021,5,24))
    print '%s days between %s and %s' % (rest_day, startdate, enddate)