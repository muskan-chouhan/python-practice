#Average of all elements in an array
def cal_avg(arr):
    total_val = sum(arr)/len(arr)
    return total_val

avg = cal_avg([1,2,3])
print(avg)


def cal(arr):
    total = 0 
    n = len(arr)
    for el in arr:
        total += el
    return total/n
print(cal([8,8,9]))

