def bubble_sort(a):
    for i in range(len(a)-1,0,-1):
        temp = True
        for j in range(0, i):
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
                temp = False
            print(a)
        if temp:
            return


a = input('Enter list elements: ').split(",")
a = [int(x) for x in a]

bubble_sort(a)

print('Sorted list: ', end='')
print(a)