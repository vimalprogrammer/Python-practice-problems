#methon overloading

class Avengers:
    def ironman(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a


s1=Avengers()
print(s1.ironman(2))

#method overriding

class A:
    def phone(self):
        print('G five')

class B(A):
    def phone(self):
        print('mi note 5')

a1=B()
a1.phone()