import face_recognition

img_path = "C:/Users/JC Austria/Documents/GitHub/Face-Recognition-Attendance-Monitoring-System/MainSystem/DataSet/Programs/BMMA/2000236246.jpg"
image = face_recognition.load_image_file(img_path)
face_locations = face_recognition.face_locations(image)
if face_locations:
    print ("existing")