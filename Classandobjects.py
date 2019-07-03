class person:
  def __init__(self,fn,ln):
    self.fn=fn
    self.ln=ln
  def printname(self):
    print(self.fn,self.ln)
class student(person):
  def __init__(self,fn,ln,yr):
    person.__init__(self,fn,ln)
    self.graduationyr=yr
  def welcome(self):
    print("welcome" ,self.fn ,self.ln, "to ", self.graduationyr)

p1=student("arav","deva",2019)
p1.printname()
p1.welcome()

import keyword
print(keyword.kwlist)
print(dir(keyword))
print()
