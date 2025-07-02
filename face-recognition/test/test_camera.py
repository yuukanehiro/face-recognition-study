import cv2

video = cv2.VideoCapture(0)
if not video.isOpened():
    raise RuntimeError("カメラが開けませんでした")

while True:
    ret, frame = video.read()
    if not ret:
        print("カメラ取得失敗")
        break

    cv2.imshow("Camera Check", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()