pos=0
def search(list,n):
    i=0
    while i<=len(list)-1:

        if list[i]==n:
            return True

        i += 1
        globals()['pos'] = i
    return False

list=[12,45,23,90,42]
n=int(input("Enter the number to be searched: "))

if search(list,n):
    print("This number is found at ",pos+1)
else:
    print('oops..! this number is not in the list')
