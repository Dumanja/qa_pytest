from tkinter import *


def display():
    if (x.get()):
        print("You agree!")
    else:
        print("You don't agree :(")


window = Tk()

x = BooleanVar()

python_photo = PhotoImage(file='Python_logo_01.svg.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')
check_button.pack()
window.mainloop()
