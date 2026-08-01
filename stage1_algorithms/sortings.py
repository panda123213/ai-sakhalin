def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
test = [64, 34, 25, 12, 22, 11, 90, 1]
print('пузырь',bubble_sort(test[:]))


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
test = [5, 2, 4, 6, 1, 3,]
print("Вставками:", insertion_sort(test[:]))


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x <=pivot]
    right=[x for x in arr[:-1] if x >pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
test = [10, 7, 8, 9, 1, 3, 5]
print("Быстрая:", quick_sort(test[:]))