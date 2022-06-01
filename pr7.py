t = (0,1,2,3,4,5,6,2,4,6,2,1)

print(max(t))
print(min(t))

s = []

for i in range(len(t)):
   if t[i] not in s:   
      print(i , " = " ,t.count(i))
   s.append(i)
   
#print the numbers in words for Example : 1234 => one two three four

t1= ("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine")

def num_to_words(n):
   if n == 0:
      return "" 
   else:
      small_num = t1[n%10];
      new_num = n // 10
      return num_to_words(new_num) + small_num + " "

n = int(input("Enter a number : "))
print(num_to_words(n))   