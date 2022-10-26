import os

path = "C:\\Users\\vrixe\\Desktop\\test\\image-dataset"
os.chdir(path)
student_folder = input("Enter new student folder:")
os.makedirs(student_folder)
