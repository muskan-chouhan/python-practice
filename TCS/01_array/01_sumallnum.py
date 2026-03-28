
arr = [5, 2, 9, 1, 7]

arr.sort()
print("smallest number is ", arr[0])



#type 2 = sorted new list return krta hai 

updatearr = sorted(arr)
print("smallest num is :", updatearr[0])


#type 3 = loop and conditon

series = [4,3,7,2,1,8,0]
min_val = series[0]
for item in series:
    if item < min_val:
        min_val = item
        print("smallest number is:", min_val)


#type 4 function using
# Function to sort the array and return the smallest element
