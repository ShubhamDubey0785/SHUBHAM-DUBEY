#Create a python program capable of greeting you withGood morning,Good afternoon and good evening. YOUR Program should use time time module to get the current time.
import time
# s=time.strftime('%H %M %S')
hour=int(time.strftime('%H'))
if hour<12 and hour>0:
    print("Good Morning sir")
elif hour>12 and hour<16:
    print("Good Afternoon sir")
elif hour>16 and hour<19:
    print("Good evening sir")
else:
    print("Good night sir")