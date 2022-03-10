from tkinter import *

# label = an area widget that holds and/or an image within a window

window = Tk()

photo = PhotoImage(file='html5-logo.png')

label = Label(window,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
# label.place(x=100, y=100)
label.pack()

window.mainloop()
