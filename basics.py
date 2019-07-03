class mechanical:
  x="Aravindan"

name=mechanical()
print(name.x)



class address:
  def __init__(self,street,door):
    self.street=street
    self.door=door
  def myfunc(self):
    print("hi this is my address  "+ self.street + self.door)
aravind=address("ttgst","5/17")
print(aravind.street)
print(aravind.door)  
aravind.myfunc()

del aravind.street
del aravind
