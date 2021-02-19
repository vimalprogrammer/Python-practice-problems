class Mart:
    def __init__(self):
        self.prod1 = 'rice'
        self.prod2 = 'wheat'
        self.prod3 = 'grain'
        self.inn=self.inner()
    def show(self):
        print(self.prod1,self.prod2,self.prod3)
        self.inn.show()


    class inner:
        def __init__(self):
            self.name='vimal'
            self.age=23
            self.duty='development'

        def show(self):
            print(self.name,self.duty,self.age)
m1=Mart()
print(m1.prod1)
lap1=m1.inn
print(lap1.name)
#lap2=Mart.inner()
#print(lap2.age)
m1.show()
