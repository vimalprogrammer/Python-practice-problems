class coder:
    def code(self):
        for i in range(4):
            for j in range(i+1):
                print('$',end=" ")
            print()
pro1=coder()
pro2=coder()
pro1.code()
pro2.code()