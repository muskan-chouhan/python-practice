arr = [9,8,7,6,5,4]

def find_second(arr):
    # Step 1: duplicates hatao
    unique = list(set(arr))
    
    # Step 2: check karo 2 values hai ya nahi
    if len(unique) < 2:
        return -1
    
    # Step 3: sort karo
    unique.sort()
    
    # Step 4: second smallest & second largest
    second_smallest = unique[1]
    second_largest = unique[-2]
    
    return second_smallest, second_largest


print(find_second(arr))


