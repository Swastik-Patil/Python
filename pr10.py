# PRQ's 
str = " hello world " + "hello"
print(str.title())
print(str.capitalize())
print(str.strip())

# Exercise

str = "This is a String With Spaces"
countUpper = 0
countLower = 0
for i in str:
   if(i.isupper()):
      countUpper = countUpper + 1
   elif(i.islower()):
      countLower = countLower + 1
print("UpperCase letters : " , countUpper)
print("LowerCase letters : " , countLower)

import random
print(random.uniform(5, 50))