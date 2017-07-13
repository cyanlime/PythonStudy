def days_plus(date,num):
    year = date[0]
    month = date[1]
    day = date[2]

    year_leap = 0
    if (year%400==0) or (year%4==0 and year%100!=0):
        year_leap = 1

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (days[month-1]-num>=day and year_leap==0) or (days[month-1]+1-num>=day and year_leap==1 and month==2):
        end_day = day+num
        return (year, month, end_day)
    
    end_year = year
    plus_days = days[month-1]-num

    if plus_days==-1 and year_leap==1 and month==2:
        return (end_year, month, days[month-1]+1)
    if plus_days==day:
        return (end_year, month, days[month-1])
    if plus_days<day:
        rest_days = num-days[month-1]+day
        if month==12:
            month%=12
            end_year+=1
        if year_leap==1 and month==2:
            rest_days-=1
        while rest_days>days[month]:
            rest_days-=days[month]
            month+=1
            if month==12 and rest_days!=0:
                month=month%12
                end_year+=1
            if ((end_year%400==0) or (end_year%4==0 and end_year%100!=0)) and month==2:
                rest_days-=1
        return (end_year, month+1, rest_days)

if __name__ == "__main__":
    days = days_plus((1994,12,31), 1)
    print days
    import datetime
    date = datetime.date(1994,12,31)+datetime.timedelta(1)
    print date