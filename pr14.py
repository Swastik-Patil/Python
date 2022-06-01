class Area:
   def area(self,len,bre):
      return 'Area of rectangle is ',(len*bre)
   def area(self,side):
      return ' Area of Square is ',(side*side)
a = Area()
print(a.area(3,2))
print(a.area(5))

class display:   
   def disp(self,int,char):
         print("Integer of first method : ",int)
         print("Character of first method : ",char)
   def disp(self,char,int):
         print("Integer of second method : ",int)
         print("Character of second method : ",char)
d = display()
d.disp('b', 2)
