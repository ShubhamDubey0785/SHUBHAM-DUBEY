#Create a python program capable of greeting you withGood morning,Good afternoon and good evening. YOUR Program should use time time module to get the current time.
import time
s=time.strftime('%H %M %S')
hour=int(time.strftime('%H'))
if hour<12 and hour>0:
    print("Good Morning")
elif hour>12 and hour<18:
    print("Good evening")
else:
    print("Good night")