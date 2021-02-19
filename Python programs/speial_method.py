class coder:
    def __init__(self,name,age,mom):
        self.name = name
        self.age = age
        self.mom = mom
    def code(self):
        for i in range(4):
            for j in range(i+1):
                print('$',end=" ")
            print()
            print("config is",pro2.name,self.age,self.mom)
pro1=coder("vimal",19,'sasi')
pro2=coder("rishi",19,'sasi')
pro1.code()

