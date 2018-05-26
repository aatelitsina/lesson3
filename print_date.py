# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime, timedelta

dt_now = datetime.now()
print('сегодня: ', dt_now)
delta = timedelta(days=1)
dt_yesterday = datetime.now()-delta
print('вчера: ' ,dt_yesterday)
delta_mn = timedelta(days=30)
dt_month = datetime.now()-delta_mn
print('месяц назад: ', dt_month)

str_time = "01/01/17 12:10:03.234567"
date  = datetime.strptime(str_time,'%d/%m/%y %H:%M:%S.%f')
print(date)