# set immutable and unodered and ignore duplicte value  and set ke element immutable hote hai 
collection = {1,2,3,4,"helloe" , "world", "world"}
print(collection)

#CREATE EMPTY SET
collectionNew = set()


#methods
#1 add  method
collectionNew.add(1)
collectionNew.add(2)
collectionNew.add(2)
collectionNew.add("muskan")   #string pass
collectionNew.add((1,2,3))    #tuple pass
# collectionNew.add([1,2,3])   #not pass buz its mutable
#2 remove methods
collectionNew.remove(1)
print(collectionNew)


#3 clear methods > set ko empty krta hai 
collectionNew.clear()
print(len(collectionNew))

#4 pop method > random value ko remove krtA hai 
collection1 = {"hello","muskan","welcome","coding","learn"}
print(collection1.pop())

#5 union method  >similar value milkar new set create kr deta hai 

set1 = {1,5,6,4,2}
set2 = {5,6,6}
print(set1.union(set2))   #new set return krega ,old set same rhege print(set1)

#6 intersection methods = common value return krgea new set
print(set.intersection(set2))
