#pivot as first element O(n^2)

"""def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l], arr[j] = arr[j], arr[l]
    return j

def quick_sort(arr, l, h):
    if l < h:
        j = partition(arr, l, h)
        quick_sort(arr, l, j - 1)
        quick_sort(arr, j + 1, h)

arr = [10, 16, 13, 5, 6, 7]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)"""

#pivot as mid element - O(nlogn)
class QuickSort:
    def partition(self, arr, low, high):
        pivot = arr[(low+high)//2]
        i = low 
        j = high
        while True:
            while arr[i] < pivot :
                i+=1
            while arr[j] > pivot :
                j-=1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def quick_sort(self, arr, l, h):
        if l < h:
            j = self.partition(arr, l, h)
            self.quick_sort(arr, l, j - 1)
            self.quick_sort(arr, j + 1, h)


arr = [10, 16, 12, 11, 6, 7, 14]
qs = QuickSort()
qs.quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)