from django.test import TestCase

# Create your tests here.
import calendar 
from calendar import HTMLCalendar
import datetime 
import sys 

time = datetime.datetime.now()
output1 = "Hi %s current time is %s " %(sys.argv[1],time)
print(output1)
'''
year = time.year
month = time.strftime('%B')
month = month.capitalize()
month_number = list(calendar.month_name).index(month)
month_number = int(month_number)

cal = HTMLCalendar().formatmonth(year, month_number)
print(cal)
#print(time)
'''





