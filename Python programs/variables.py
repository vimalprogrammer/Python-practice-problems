class bike:

    wheels=3#class variable/static variable
    def __init__(self):
         self.mil=67 #instance variable
         self.cc=200


c1=bike()
c2=bike()
c1.wheels=8
print(c1.cc,c2.wheels)
