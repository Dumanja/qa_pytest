from tkinter import *


def doSomething(event):
    #print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

#window.bind("<Return>", doSomething)        # return = Enter
#window.bind("<q>", doSomething)
window.bind("<Key>", doSomething)           # Key = All

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()