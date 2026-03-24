#question 1
dic = {
    "table" : ["a piece of furniture","list of fact & figures"],
    "cat"  : "a samll animal"
}

print(dic)


#question 2  >set

subject = {"python","java", "c++","python", "javascript","java","python","java","c++","c"}
print(len(subject))


#question 3

marks = {}

x = int(input("enter physics marks :"))
y = (input("enter chemestry marks :"))
z = (input("enter maths marks :"))

marks.update({"phy" : x,"chm" : y, "maths": z})

print(marks)

#question 4

set = {4, "9.0", 8.8, }
print(set)

#second posible solution

values = {
    ('float',9.0),
    ('int',3)
}
print(values)