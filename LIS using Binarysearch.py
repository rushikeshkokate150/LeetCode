import bisect

arr = [1,7,8,4,5,6,-1,9]

arr1 = []
arr1.append(arr[0])

for i in range(1,len(arr)):
    if arr[i] > arr1[-1]:
        arr1.append(arr[i])
    else:
        ind = bisect.bisect_left(arr1,arr[i])
        arr1[ind] = arr[i]
print(len(arr1))
    