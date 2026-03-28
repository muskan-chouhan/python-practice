
arr = [1, 2, 2, 3, 1, 4, 2]

freq = {}

for el in arr:
    if el in freq:
        freq[el] += 1
    else:
        freq[el] = 1

for key in freq:
    print(key, "->", freq[key])

