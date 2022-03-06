# str.format() =    optional method that  gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item)) #posititnal argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Marko"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 3.14159
number2 = 1000

print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number2))
print("The number is {:b}".format(number2))
print("The number is {:o}".format(number2))
print("The number is {:X}".format(number2))
print("The number is {:E}".format(number2))