#Check if a number is Palindrome or Not - Problem Statement: Given an integer N, return true if it is a palindrome else return false.


n = 121

original = n
rev = 0

while n > 0:
    digit = n % 10             #digit = 121 % 10 = 1
    rev = rev * 10 + digit     #rev = 0 *10 + 1 = 1
    n = n // 10                #n = 121 // 10 = 12

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


 #find in range 

for i in range(10, 200+1):

    num = i
    rev = 0

    while num > 0:
        digit = num % 10             
        rev = rev * 10 + digit     
        num = num // 10   
    if i == rev:
        print(i)
