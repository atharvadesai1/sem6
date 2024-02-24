import random

def partition(a, lb, hb):
    pivot = a[lb]
    i = lb
    j = hb
    while i<j:
        while a[i]<=pivot:
            i+=1
        while a[j]>pivot:
            j-=1
        if i<j:
            a[i] ,a[j] = a[j], a[i]
    
    a[lb] , a[j] = a[j] , a[lb]
    return j

def quicksort(a, lb, ub):
    if lb < ub:
        pivot_index = random.randint(lb,ub)
        a[lb] , a[pivot_index] = a[pivot_index], a[lb]
        pivot_index = partition(a, lb, ub)
        quicksort(a, lb, pivot_index-1)
        quicksort(a, pivot_index+1, ub)
    return a

print('***************RANDOMIZED QUICK SORT***************')
print()
n = int(input('Enter the number of elements in array: '))
print('Enter the elements of array: ')
a = list(map(int, input().split()))[:n]
print()
print(f'Elements of Array: {a}')
sorted_array = quicksort(a, 0, n-1)
print(f'Sorted Array using Quick Sort: {sorted_array}')
