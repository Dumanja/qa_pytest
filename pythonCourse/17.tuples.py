# tuples =  collection which is ordered and unchangeable
#           used to group together related data

student = ("Marko",22,"male")

print(student.count("Marko"))
print(student.index("male"))

for x in student:
    print(x)

if "Marko" in student:
    print("Marko is here!")