# Python program to implement Selection sort

def selection_sort(a):
    for i in range(0, len(a) - 1):
        first = i
        for j in range(i + 1, len(a)):
            if a[j] < a[first]:
                first = j
        a[i], a[first] = a[first], a[i]
a = input('Enter list elements: ').split()
a = [int(x) for x in a]
selection_sort(a)
print('Sorted list: ', end='')
print(a)