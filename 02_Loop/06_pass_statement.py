# pass use if you do not want to do anything
for i in range(5):
    pass
print("end")


#q sum vo n number using while 

n = 5
sum = 0
for i in range(1,n+1):
    sum += i
print("total sum of = ",sum)

#q find factorial of natural number using loop 

n = 5
fact = 1
i = 1
for i in range(1,n+1):
    fact *= i
    i += 1
    print(fact)
