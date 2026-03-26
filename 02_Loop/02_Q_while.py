#question 1
count = 1
while count <= 100:
    print(count)
    count += 1
print("end")

#question 2
count = 100
while count >= 1 :
    print(count)
    count -= 1
print("end")

#question 2  /table of randum number

num = int(input("enter number"))
i = 1
while i <= 10:
    print(num * i)
    i += 1
print("end of table")


#q3

list = [1,4,9,16,16,39,199,8,9,3]
idx = 0
while idx <= len(list)-1:
    print(list[idx])
    idx += 1
print("all element")    

heros = ["ironman","thor","batman"]
idx = 0

while idx < len(heros):
    print(heros[idx])
    idx += 1

print("all element")

#q
x=44
tuple = (11,22,33,44,55,66,77,88,44)
i = 0
while i< len(tuple):
    if(tuple[i] == x):
        print("found at index",i)
        break
    else:
        print("finding",i)

    i += 1   

 #example using break
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break

    i += 1   
print("complete")
 #example using continue
i = 1
while i < 5:
    if(i == 3):
        i += 1 
        continue
    print(i)
    i += 1 

 #q odd print
i = 1
while i < 10:
    if(i % 2 == 0):    # if(i % 2 != 0): even
        i += 1 
        continue
    print(i)
    i += 1 
      