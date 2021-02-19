def sayhi(name):
    print(name+' hi')


try:
    sayhi(7)
except Exception as e:
    print("wrong type" ,e)
finally:
    print('ba bye')