#Find the median of the given array
arr = [1,4,3,6,8,]
arr.sort()
n = len(arr)
mid = n//2
if(n% 2 == 0):
    avg = (arr[mid-1]+arr[mid])/2
    print(avg)
else:
    print(arr[mid])

def getMedian(arr):
    n = len(arr)
    if(n% 2 == 0):
        ind1 = (n // 2) - 1
        ind2 = (n // 2)
        print((arr[ind1] + arr[ind2]) / 2)
    else:
        print(arr[n // 2])

getMedian([3,5,6,2,5])        