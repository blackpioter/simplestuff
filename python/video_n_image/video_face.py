import cv2

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    print(check)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",frame)
    cv2.imshow("Capturing_gray",gray)

    key=cv2.waitKey(100)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()
