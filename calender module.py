import calendar
date=list(map(int,input().split()))
weekday={}
weekday[0]='MONDAY'
weekday[1]='TUESDAY'
weekday[2]='WEDNESDAY'
weekday[3]='THURSDAY'
weekday[4]='FRIDAY'
weekday[5]='SATURDAY'
weekday[6]='SUNDAY'
print(weekday[calendar.weekday(date[2], date[0], date[1])])
