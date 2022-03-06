# slicing = create a substring by extracting elements from another string
# indexing[] of slice()
# [start:stop:step]

name = "Bug Sekeer"

first_name = name[:3]           # [0:3] = [:3]
last_name = name[4:10]          # [4:10] = [4:] in this example
funky_name = name[0:10:2]       # [::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
