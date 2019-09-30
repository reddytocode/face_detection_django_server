import requests
import cv2


url = "http://127.0.0.1:8000/face_detection/detect/"

image = cv2.imread("images/boy.jpg")
payload =  {'image': open('images/boy.jpg', 'rb')}
r = requests.post(url, files=payload).json()
print(r)
#a = {"success": true, "num_faces": 1, "faces": [[190, 227, 827, 864]]}
for (x1, y1, x2, y2) in r["faces"]:
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite("out.jpg", image)
cv2.waitKey(0)