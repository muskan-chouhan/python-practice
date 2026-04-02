#Check if a number is prime or not

n = 5
count = 0 
for i in range(1, n+1): # 1 aur n ke alawa koi aur number divide kar raha hai ya nahi
    if n % i == 0:    #4 % 1 == 0 => 0  , 4 % 2  == 0 , 2 
        count += 1    # count = 0 +1 = 1  count = 2

if(count == 2):
    print("prime")
else:
    print('not prime')    
          

#2q Prime Numbers in a given range

a = 10
b = 20

a = 10
b = 20

for i in range(a, b+1):

    if i <= 1:
        continue

    count = 0

    for j in range(1, i+1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(i)

