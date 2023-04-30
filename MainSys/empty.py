
import cv2

cap = cv2.VideoCapture(0)

# get supported resolutions
resolutions = []
for i in range(400):
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH + i)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT + i)
    if width == 0 or height == 0:
        break
    resolutions.append((width, height))

# find first supported resolution with aspect ratio of 16:9
for width, height in resolutions:
    if abs(width / height - 16 / 9) < 0.01:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        break

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(resolutions)
        break

cap.release()
cv2.destroyAllWindows()