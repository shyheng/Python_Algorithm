import calendar

c = calendar.calendar(2020)
print(c) #打印2020日历

print(calendar.isleap(2020))#判断是否闰年，是返回true
print(calendar.leapdays(1600,2330)) #获取之间有多少个闰年
print(calendar.month(2019,3))#打印2019年3月的日历

