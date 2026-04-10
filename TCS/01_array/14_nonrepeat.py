# Find all the non-repeating elements in an array
arr = [1,4,2,1,2,4,2]
def findRepeating(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                print(arr[i])
                break   # same element baar-baar print na ho


arr = [1,2,3,2,4,1,5]
findRepeating(arr);


