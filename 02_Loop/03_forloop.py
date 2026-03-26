#for loop >travesing sequence se hoti hai . index ka us enhi hota
nums = [1,2,3,4]
for val in nums:
    print(val)

 #example for loop using list

fruits = ["apple","banana","chery"]
for val in fruits:
    print(val)  

#example for loop using tuple

tup = (11,22,33)
for num in tup:
    print(num)     

#example for loop using string
str = "apnaDewas"
for chr in str:
    if(chr == "D"):
        print("D found")
        break
    print(chr)
else:
    print("end")    