# multi-level inheritance = when a derived (child) class inherts another derived (child) class

class Organisam:
    alive = True


class Animal(Organisam):

    def eat(self):
        print("This animal is eating")


class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
