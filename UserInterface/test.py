from sre_parse import State
from tkinter import *

#tk name of window
root = Tk()
root.geometry("1280x720")

def myClick():
    myLabel1 = Label(root, text= "Hello World!")
    myLabel1.pack()

myButton2 = Button(root, text = "Click Me !", command=myClick ).grid(row=0, column=1)
myButton1 = Button(root, text = "Click Me !", command=myClick ).grid(row=0, column=0)
# Creating a Label Widget
myLabel1 = Label(root, text= "Hello World! My Name is JC").grid(row=1, column=0,columnspan=2)
#myLabel2 = Label(root, text= "My name is  JC!").grid(row=0, column=1)
# putting the widget to root (screen)
#myLabel1.grid(row=0, column=0)




root.mainloop()