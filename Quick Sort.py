arr = [4,6,2,5,7,9,1,3]

def partition(left,right):
    j = left-1
    pivat = arr[right]
    for i in range(left,right):
        if arr[i] <  pivat:
            j += 1
            arr[j],arr[i] = arr[i],arr[j]
    j+=1
    arr[j],arr[right] = arr[right],arr[j]
    return j

def quicksort(left,right):
    if left<right:
        p = partition(left,right)
        quicksort(left,p-1)
        quicksort(p+1,right)

quicksort(0,len(arr)-1)
print(arr)

    