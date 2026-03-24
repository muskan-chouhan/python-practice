#List
marks = [22,23,44,55,56]
print(marks)
print(type(marks))               #type of
print(len(marks))                #total length

#access index
print(marks[0])   #output = 22
print(marks[1])


student = ["ram",22.4, "delhi"]    #string   inmutable and list mutable hoti hai 
print(student)
student[0] = "kisan"
print(student)  #new list 


#slicing
print(marks[0:3])
print(marks[:3]) #automatic starting
print(marks[1:]) #automatic end 
print(marks[-3:-1])

#append method
list = [2,1,3]
list.append(4)
print(list)       #output = [2,1,3,4]

#sorting method  > assending order mai arrange kr deta hai >chote se bda
list.sort()
print(list)

#reverse(disending) order mai sort krwana ke liye  

list.sort(reverse=True)
print(list)

#example with character
list1 = ["apple","chery","banana"]
list1.sort()
print(list1)         #output = ["apple","banana","chery"]

#reverse method
list2 = ["c","b","a"]
list2.reverse()
print(list2)               #output = ["a","b","c"]

#insert methods > middel konse index pr add krna hai 
list3 = [2,3,4]
list3.insert(1,0)
print(list3)           #output =    [2,0,4]


#remove method  >particular remove number
list3.remove(2)
print(list3)       #output =    [0,4]

#pop method  > index se remove
list5 = [1,2,3,4,6]
list5.pop(1)
print(list5)         #output = [1,3,4,6]


#question practice
movieList =  []
movie1 = input("enter your 1 frvt movie ")
movie2 = input("enter your 2 frvt movie ")
movie3 = input("enter your 3 frvt movie ")

movieList.append(movie1)
movieList.append(movie2)
movieList.append(movie3)
print(movieList)



#q2  > palindrom
list_1 = [1,2,1]
list_2 = [1,2,3]

copy_list1 = list_1.copy()
copy_list1.reverse()

if(copy_list1 == list_1):
    print("palindrom")
else:
    print("not palindrom")
