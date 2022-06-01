#PRQ's

import math

print(math.sqrt(25))
print(math.pi)
print(math.degrees(2))
print(math.radians(60))
print(math.sin(2))
print(math.cos(0.5))
print(math.tan(0.23))
print(math.factorial(4))

print()
print()

import random
print(random.randint(0, 5))
print(random.random())
print(random.random()*100)

List = [1,4,True,800,"Python",27,"hello"]
print(random.choice(List))

print()
print()

import datetime
from datetime import date
import time
print(time.time())
print(date.fromtimestamp(454554))

print()
print()

#Exercise
import new_module

import math
radius = int(input("Enter the radius of the circle : "))
print("Area of Circle is ",math.pi*radius**2)
print("Circumference of Circle is ",2*math.pi*radius)

import calendar
month = int(input("Enter the month : "))
print(calendar.month(2022,month))
