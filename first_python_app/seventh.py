# import datetime
 
# dt = datetime.datetime.now()

# unmoghe  = datetime.timedelta(120)

# x = dt.strftime('%X')
# # y = dt.strftime('%a')

 
# print(x)
# # print(y)

from khayyam import JalaliDatetime,JalaliDate

dt = JalaliDatetime.now().strftime('%B')

print(dt)