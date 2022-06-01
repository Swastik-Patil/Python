
def add(x,y):
   sum = x + y 
   print("Addition of ",x," and ",y ," is ",sum)
   
add(4,5)

def factorial(num):
   if( num == 0 or num == 1):
      return 1
   else:
      return num * factorial(num-1)     # Recursive Function

print(factorial(10))

