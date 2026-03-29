#i = 0 → arr[i] = 1 (first unique)
#j = 1 → next element check karega

def removeDuplicates(arr):
    if len(arr) == 0:
        return 0

    i = 0   #arr[i]=1 ,arr[j]=1 after i = 1

    for j in range(1, len(arr)):  # fast pointer
        if arr[j] != arr[i]:       # 1 =! 1 after  2 != 1 after 2!= 1
            i += 1                                 # i = 0+ 1    , i = 1
            arr[i] = arr[j]                        # array mai arr[1] = arr[2], 1 index  = 2

    return i + 1


# Test
arr = [1,1,2,2,3,4,4]
k = removeDuplicates(arr)

print("k =", k)
print("array =", arr[:k])         