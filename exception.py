class Error(Exception):
   def moreThanTen(self,a,b):
      self.a = a
      self.b = b
      try:
         c = self.a + self.b
         if(c < 10):
            raise Error
         else:
            print(c)
      except Error:
         print("Value of c is less than 10")
         
M = Error()
M.moreThanTen(6, 5)
M.moreThanTen(5,0)
