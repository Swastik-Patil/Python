num = 5
if num > 0:
   print("Number is Positive")

age = 21
if age > 18 :
   print("Eligible for voting")
else:
   print("Not Eligible for voting")

s1,s2,s3,s4,s5 = 86,92,97,93,88
avrg = (s1 + s2 + s3 + s4 + s5)/5

if(avrg <= 100 and avrg > 75):
   print("First Class Distinction")
elif(avrg < 75 and avrg > 60):
   print("First Class")
elif(avrg < 60 and avrg > 40):
   print("Pass Class")
elif(avrg < 40 and avrg >= 0):
   print("Fail")
else:
   print("Invalid Marks")
   
   
