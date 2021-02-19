# Python program to implement Insertion sort

def insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while (j >= 0 and temp < a[j]):
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = temp


a = input('Enter list elements: ').split()
a = [int(x) for x in a]

insertion_sort(a)

print('Sorted list: ', end='')
print(a)