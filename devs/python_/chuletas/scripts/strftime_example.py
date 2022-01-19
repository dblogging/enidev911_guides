# ======================================
# date class : to work with date
# time class : to work with time
# datetime class : combination of date and time classes

import datetime as dt 

#current_date = dt.date.today()
#print(current_date)

#y, m, d = input("Birthday: (YYYY-MM-DD) ").split("-")
#date1 = dt.date(int(y), int(m), int(d))

#print(date1)


# current date and time
now = dt.datetime.now()

year = now.strftime("%Y")
print("año: ", year)

month = now.strftime("%m")
print("mes: ", month)

day = now.strftime("%d")
print("día: ", day)

time = now.strftime("%H:%M:%S")
print("hora: ", time)


date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("fecha y hora: ", date_time)


timestamp = 1528797328
date_time = dt.datetime.fromtimestamp(timestamp)


print("Date time object: ", date_time)
print(date_time.strftime("%a"))

#import calendar
 
#cal = calendar.month(2018, 2)
#print ("Aquí está el calendario:", cal)
 