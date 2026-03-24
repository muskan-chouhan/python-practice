light = "blue"

if(light == "green"):
     print("continue")
elif(light =="red"):
     print("stop")
print("end of code")


#nesting


#question 1
number = int(input("enter  number"))

if(number%2 == 0):
     print("even")
else:
     print("odd")

#question 2

num1 = int(input("enter  number 1"))
num2 = int(input("enter  number 2"))
num3 = int(input("enter  number 3"))

if(num1 >= num2 and num1 >= num3):
     print(num1,"is greatest number")
elif(num2 >= num3):
     print(num2,"is greatest number")
else:
     print(num3,"is greatest number")