import calendar

calendar_calendar = calendar.calendar(2018)
print(calendar_calendar)

print("*"*29)
print(calendar.calendar(2018,1,2,10))

print(calendar.isleap(2028))
print(calendar.leapdays(2000, 2020))

print(calendar.month(2018, 12))

print(calendar.monthcalendar(2018, 12))

print(calendar.weekday(2018, 12, 1))