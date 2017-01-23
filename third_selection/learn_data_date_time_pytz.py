#!/usr/bin/env python

from datetime import datetime
from pytz import timezone
import pytz

d = datetime(2017, 1, 23, 10, 17, 0)
print (d)

central = timezone("US/Central")
loc_d = central.localize(d)
print (loc_d)

bang_d = loc_d.astimezone(timezone("Asia/Kolkata"))
print (bang_d)

"""

将时间统一转换为UTC时间，然后在获取时区

"""
utc_d = loc_d.astimezone(pytz.utc)
print (utc_d)

#北京时间'Asia/Shanghai'
print (pytz.country_timezones['cn'])

central = timezone('Asia/Shanghai')
loc_shanghai = central.localize(datetime.now())
print (loc_shanghai) # 上海时间 ->2017-01-23 10:34:56.764935+08:00 （+8表示比UTC快8个小时）