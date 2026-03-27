#1. q
cities = ["Delhi", "Pune", "Noida","Gurgaon","Mumbai","Chennai"]
heroes = ["Thor", "Ironman", "captain america"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#2. q

name = ["Ram","Anjali","Sneha"]

def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(name)      
print()  #for ignore %

#3. q factorial 

def cal_fac(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fac(8)

#4 usd convert itno inr

def converter(usd_val):
     inr_val = usd_val * 83
     print(usd_val,"USD =", inr_val, "INR" )
converter(100)   

 
def checker(val):
    if(val%2 == 0):
        print("even")
    else:
        print("odd")
checker(3)           