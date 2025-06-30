import sys
import face_recognition
import cv2
import numpy as np
from PIL import imageFont, ImageDraw, Image
import glob

video_capture = cv2.VideoCapture(0)

def main():
    while True:
        # ビデオの単一フレームを取得
        _, frame = video_capture.read()

        # 結果をビデオに表示
        cv2.imshow('Video', frame)

        # ESCキーで終了
        if cv2.waitKey(1) == 27:
            break

main()

# ビデオキャプチャを解放し、ウィンドウを閉じる
video_capture.release()
cv2.destroyAllWindows()