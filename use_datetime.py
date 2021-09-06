#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re
from datetime import datetime, timedelta, timezone, tzinfo

#获取当前datetime
now = datetime.now()
print('now = ', now)
print('type(now) = ', type(now))

#用指定日期时间创建datetime
dt = datetime(2015, 4, 19, 12, 20, 20)
print('dt = ', dt)

#吧datetime转换为timestamp
print('datetime -> timestamp: ', dt.timestamp())

#把timestamp转换为datetime
t = dt.timestamp()
print('timestamp -> datetime：', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0；', datetime.utcfromtimestamp(t))

#从str读取datetime
cday = datetime.strptime('2021-09-06 10:23:20', '%Y-%m-%d %H:%M:%S')
print('strptime : ', cday)

#把datetime格式化输出
print('strftime: ', cday.strftime('%a, %b %d %H:%M'))

#对日前进行加减
print('current datetime = ', cday)
print('current + 10 hours= ', cday + timedelta(hours=10))
print('current - 1 day= ', cday - timedelta(days=1))
print('current + 2.5 days = ', cday + timedelta(days=2, hours=12))

#把时间从UTC+0 时区转换为UTC+8
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now = ', utc_dt)
print('UTC+8:00 now = ', utc8_dt)


#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
def to_timestamp(dt_str, tz_str):
    rtdatetime = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    a = re.match(r'^UTC([\+\-])(\d+)\:[0-5][0-9]$', tz_str)
    str_hour = a.group(1) + a.group(2)
    print(str_hour)
    tz = timezone(timedelta(hours=int(str_hour)))
    utcStr_rt = rtdatetime.replace(tzinfo=tz)
    return utcStr_rt.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')