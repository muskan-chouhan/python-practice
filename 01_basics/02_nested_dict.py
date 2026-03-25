student = {
    "name" : "kashish chouhan",
    "subject" : {
        "php" : 55,
        "java" : 77,
        "js"  : 55     
    }
}

print(student["subject"]['java'])

# DICTIONARY METHODS

#1 keys methods  =>  ALL KEY ACCESS    
print(student.keys())
#type casting 
print(list(student.keys()))
#total number  of keys
print(len(student))

#2 values methods  => =
print(list(student.values()))


#3 . items methods  => = pair form mai deta hai 
pairs = list(student.items())
print(pairs[0])

#4 .get methods  =>
print(student['name'])
print(student.get('name'))

#5 upadte method
new_dict = student.update({"city" : "dewas"})
print(new_dict)