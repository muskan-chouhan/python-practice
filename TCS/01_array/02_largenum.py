arr = [9,2,3,4,7,6]

def cal_large(arr):
    max_val = arr[0]   # 👈 andar le aa

    for num in arr:
        if num > max_val:
            max_val = num

    print("largest number is", max_val)  
cal_large(arr)


#type  2
arr1 = [22,44,66,77,88]
def sortArr(arr1):
    arr1.sort()
    return arr1[-1]

result = sortArr(arr1)
# print(result)
print("The Largest element in the array is:", sortArr(arr1))