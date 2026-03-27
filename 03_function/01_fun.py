def cal (a,b):
    sum = a + b
    print(sum)        
    return sum
cal(2,3)     
cal(4,7  
      )

def calc (a,b):
    return a*b
sum = calc(5,6)
print(sum)


#q avrage of 3 numbers
def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum / 3
    print(avg)
    return avg
cal_avg(2,2,2)

#default parameter
def cal_sum(a=1,b=1):
    print(a+b)
    return a+b
cal_sum()