# **kwargs =    parameter that will pack all arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments
import kwargs as kwargs


def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])

    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")


hello(title="Mr.",first="Marko", middle="Marcuss", last="Topalović")