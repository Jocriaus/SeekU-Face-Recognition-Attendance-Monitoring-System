from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter import filedialog

Tk().withdraw()

file_empty = True
while (file_empty):
    file_select = filedialog.askopenfilename()
    if file_select == "":
        file_empty = True
    else:
        file_selected = file_select
        file_empty = False

if file_selected.endswith('.jpg'):     
    print(file_selected)


