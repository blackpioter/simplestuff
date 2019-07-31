import cv2
import os

for item in os.listdir("sample-images"):
    if not "resized_" in item and item.endswith(".jpg"):
        print("Resizing: ",item)
        img=cv2.imread("sample-images/"+item,1)
        resized_image=cv2.resize(img,(100,100))
        cv2.imwrite("sample-images/resized_"+item,resized_image)
    else:
        print("Skipping: ",item)
