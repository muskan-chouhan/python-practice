info = {
    "name" : "Nikita",
    "cgpa" : 88.23,
    "learning" : "Web Devoping",
    "is_adult" : True,
    "subject" : ['python',"PHP", "Wordpess"],        #list
    "topics" : ("dict" , "set"),                     #tuple
     12.0 : "23.3"                                            
}
print(info)


#access value

print(info["name"])
print(info["learning"])
print(info["subject"])
print(info["topics"])
print(info["cgpa"])


#asign new values
info['name'] = "anya"   #overwrite
print(info)

#add new key and value
info['surname'] = "sharma"
print(info)

#empty dict create
null_dict = {}
null_dict['name'] = "kashish chouhan"
print(null_dict)