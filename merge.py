arr= [3,1,2,4,1,5,2,6,4]
def merge(arr1,arr2):
    i = 0
    j = 0
    newarr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newarr.append(arr1[i])
            i+=1
        else:
            newarr.append(arr2[j])
            j+=1
    while i < len(arr1):
        newarr.append(arr1[i])
        i+=1
    while j < len(arr2):
        newarr.append(arr2[j])
        j+=1
    return newarr
    
def mergersort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergersort(arr[:mid])
    right = mergersort(arr[mid:])
    return merge(left,right)
    

print(mergersort(arr))


    