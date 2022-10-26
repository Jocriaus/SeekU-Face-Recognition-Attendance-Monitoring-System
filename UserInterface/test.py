from tkinter import *

#tk name of window
root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text= "Hello World!")
myLabel2 = Label(root, text= "My name is  JC!").grid(row=0, column=1)
# putting the widget to root (screen)
myLabel1.grid(row=0, column=0)



root.mainloop()