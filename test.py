# # add two numbers together and return the result
# def add(a, b):
#     print(a + b) # print the result
# add(5, 6)

# find square root of a number  and return the result
def square_root(num):
    print(num ** 0.5)
square_root(25)

print("Enter three numbers :")
x,y,z = map(int, input().split())
largest = max(x,y,z)
print(largest)

num = 1
while num <= 100:
   if num%2 == 0:
      print(num)
   num += 1
   
rows,k,n,num = 5,1,1,0
for i in range(1,rows):
   if(rows%2==0):
      num = 0
   else:
      num = 1
   for j in range(1,k+1):
      print(end = " ")
   k =  k + 1
   while n <= (2* (rows - i) - 1):
      if num == 1:
         print("1",end = "")
         n = n + 1
         num = 0
      else:
         print("0",end = "")
         n = n + 1
         num = 1
   n = 1
   print()