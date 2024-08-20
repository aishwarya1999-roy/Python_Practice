def merge(arr,mid,s,e):
    mid=(s+e)//2
    left = arr[s:mid+1]
    right = arr[mid+1:e+1]
    i= j = 0
    k = s
    for i in range(size1):
        left[i] = arr[k]
        k+=1

    k = mid+1
    for i in range(size2):
        right[i] = arr[k]
        k+=1
    ind1 = 0
    ind2 = 0
    k = s   
    while ind1<size1 and ind2<size2:
        if (left[ind1]<right[ind2]):
            arr[k] = left[ind1]
            k+=1
            ind1+=1
        else:
            arr[k] = right[ind2]
            k+=1
            ind2+=1

def merge_sort(arr, s,e):
    if s>=e:
        return
    mid = (s+e)//2
    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    merge(arr,mid,s,e)

arr = [55, 16, 9, 23, 1, 12, 3]
n = len(arr)
merge_sort(arr, 0,n-1)

for i in range(n):
    print(arr[i])