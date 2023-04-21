path = "C:/Users/JC Austria/Documents/GitHub/Face-Recognition-Attendance-Monitoring-System/MainSystem/user_create.py"
newpath = ""
for char in path:
    if char == "/":
        newpath += "\\"
    else:
        newpath += char

print(newpath)