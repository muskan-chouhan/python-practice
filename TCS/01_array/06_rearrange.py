
#type
arr = [8, 7, 1, 6, 5, 9]

arr.sort()
mid = len(arr) // 2

first = arr[:mid]
second = arr[mid:]

second.reverse()

print(first + second)