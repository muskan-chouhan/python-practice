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

#ALL KEY ACCESS
print(student.keys())
#type casting 
print(list(student.keys()))


#total number  of keys
print(len(student))