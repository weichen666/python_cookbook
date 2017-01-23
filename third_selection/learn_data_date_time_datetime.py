#!/usr/bin/env python

from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print (c) #->2 days, 10:30:00
print (c.days) #->2
print (c.seconds) #->37800
print (c.seconds / 3600) #->10.5
print (c.total_seconds()/ 3600) #->58.5



from datetime import datetime
a = datetime(2017, 1, 17)
#加多少天
print (a + timedelta(days=22))

#减多少天
print (a + timedelta(days=-22))

now = datetime.today()
print (now)
print(now + timedelta(minutes=10))

# datetime 会自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print (a - b) 


"""
dateutil 模块
	执行更加复杂的日期操作。
"""


from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
	'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
	if start_date is None:
		start_date = datetime.today()
	#星期一索引为0
	day_num = start_date.weekday()
	day_num_target = weekdays.index(dayname)
	days_ago = (7 + day_num - day_num_target) % 7
	if days_ago == 0:
		days_ago = 7
	target_date = start_date - timedelta(days=days_ago)
	return target_date

print (get_previous_byday('Monday'))



from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
	if start_date is None:
		start_date = date.today().replace(day=1)
		
		#monthrange 找到改月的总天数
	_, days_in_month = calendar.monthrange(start_date.year, start_date.month)
	end_date = start_date + timedelta(days=days_in_month)
	return (start_date, end_date)

frist_day, last_day = get_month_range()
print(frist_day)
print(last_day)

a_day = timedelta(days=1)
while frist_day < last_day:
	print(frist_day)
	frist_day += a_day

