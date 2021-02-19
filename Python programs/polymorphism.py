#Duck typing

class Home:
    def at(self):
        print('he is rude')
        print('he is foodie')


class School:
    def at(self):
        print('he is excellent')
        print('he is very sportive')


class College:
    def at(self):
        print('he is attractive')
        print('he is very brilliant')


class Behaviour:
    def code(self,vimal):
        vimal.at()

ide=College()
c1=Behaviour()
c1.code(ide)

print()
print(90*"-",end="")

