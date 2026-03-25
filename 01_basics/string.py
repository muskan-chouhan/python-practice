str = "apna clg"
ch = str[1]
print(ch)  #output > p

#slicing  > tukde krna 
#syntax  = str[1st : end]   end index include nhi hoga 

str1 = "Apna college"
newStr = str1[5 : 12]  # str1[5:len(str)]
print(newStr)


#substring*) >check  krta hai string konse character pr  end ho rhi hai ya nhi 

str = "i am studing in room"
print(str.endswith("om"))  #output >true


#capitalize first charter
str  = "muskan"
print(str.capitalize())  #new string mai chnge krta hai purni mai nhi  krt hai 


#replace
str  = "muskan chouhan"
print(str.replace("a","@"))


#check krta hai kis index  pr  vo charcter aata hai 

str  = "muskan chouhan"
print(str.find("a"))  #output = 4
print(str.find("chouhan")) #output = 7

#count >count krega kitne tym aarha hai 
str  = "is muskan chouhan from dewas or from indore"
print(str.count("from"))
print(str.count("o"))


#question
name = input("enter your name")
print(len(name),name)



