class person:
  def __init__(self,fn,ln):
    fn=self.fn
    ln=self.ln
  def printname(self):
    print(self.fn,self.ln)
class student(person):
  def __init__(self,fn,ln,yr):
    person.__init__(self,fn,ln)
    self.graduationyr=yr
p1=person("arav","deva")
x.printname()
