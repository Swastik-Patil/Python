class Student:
   def read(self,name,roll):
      self.name = name
      self.roll = roll

class Write(Student):
   def printDetails(self):
      print("Name:",self.name)
      print("Roll:",self.roll)

w = Write()
w.read("Swastik", "3356")
w.printDetails()

class A:
   def A(self):
      print("A")

class B: 
   def B(self):
      print("B")
      
class C(A,B):
   def C(self):
      print("C")
   
c = C()
c.A()
c.B()
c.C()
