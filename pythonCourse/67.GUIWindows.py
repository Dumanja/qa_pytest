from tkinter import *

# windows = GUI elements: buttons, textboxes, labels, images
# widgets = serves as a container to hold or contain widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Marko's first GUI program")

icon = PhotoImage(file='cover.png')
window.iconphoto(True,icon)
window.config(background="#19286E")

window.mainloop() #place window on computer screen, listen for events
