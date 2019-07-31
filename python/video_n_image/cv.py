import cv2

img=cv2.imread("galaxy.jpg",0)
print(img.shape[1], img.shape[0], img.ndim)

cv2.imshow("Galaxy",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()


resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

print(resized_image.shape[1], resized_image.shape[0], resized_image.ndim)
cv2.imshow("Resized",resized_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite("Galaxy_resized.jpg",resized_image)
