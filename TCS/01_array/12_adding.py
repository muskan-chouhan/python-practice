arr = [2,3,4]
arr.insert(0,1)# Function to insert at beginning of array
arr.append(5)  # Function to insert at end of array

arr.insert(2,99)   # Function to insert at a given position (0-based index)
print(arr)

def insertAtBeginning(arr1, x):
    arr1.insert(0, x)
    return arr1
result = insertAtBeginning([22,33,44],11)
print(result)

def insertAtEnd(arr, x):
        arr.append(x)
        return arr

result = insertAtEnd([22,33,44], 55)
print(result)

def insertAtPosition(arr, pos, x):
        arr.insert(pos, x)
        return arr

arr = insertAtPosition([11,22,33,44], 3, 66)
print(arr)
