import cv2
import dlib
import os

# 顔検出器の読み込み
detector = dlib.get_frontal_face_detector()

# ニューラルネットワークオブジェクト生成
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000_fp16.caffemodel')

# 顔画像ディレクトリ
dataset_dir = "known_faces"
face_images = {}

print("🔍 known_faces フォルダ内の画像を読み込み中...")

for filename in os.listdir(dataset_dir):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    name = os.path.splitext(filename)[0]
    path = os.path.join(dataset_dir, filename)
    image = cv2.imread(path)

    if image is None:
        print(f"⚠️ 読み込み失敗: {filename}")
        continue

    face_images[name] = image
    print(f"✅ 登録: {name}")

# カメラキャプチャの開始
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("❌ カメラが開けませんでした")

print("🎥 顔認識を開始します（ESCで終了）")

while True:
    ret, img = cap.read()
    if not ret:
        print("❌ カメラからフレームを取得できませんでした")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_roi = img[y:y + h, x:x + w]
        if face_roi is None or face_roi.size == 0:
            print("顔領域が空です")
            continue

        blob = cv2.dnn.blobFromImage(face_roi, 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()

        confidence = detections[0, 0, 0, 2]
        if confidence > 0.5:
            max_similarity = -1.0
            max_name = 'Unknown'

            # 登録済みの顔写真とのループ比較
            for name, face_image in face_images.items():
                if face_image is None:
                    continue

                # 顔サイズの調整 比較する為に同じサイズにするs
                face_image_resized = cv2.resize(face_image, (face_roi.shape[1], face_roi.shape[0]))

                # ヒストグラム計算（輝度分布）
                hist1 = cv2.calcHist([face_roi], [0], None, [256], [0, 256])
                hist2 = cv2.calcHist([face_image_resized], [0], None, [256], [0, 256])

                # ヒストグラムの正規化
                cv2.normalize(hist1, hist1)
                cv2.normalize(hist2, hist2)

                # ヒストグラム比較
                similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

                # 最も高い類似度の人物を記録
                if similarity > max_similarity:
                    max_similarity = similarity
                    max_name = name

            # 類似度を 0-100 スケールに変換（HISTCMP_CORREL は -1〜1）
            similarity_score = int((max_similarity + 1) * 50)  # [-1,1] → [0,100]

            label = f"{max_name} ({similarity_score}%)" if max_name != 'Unknown' else "Unknown ❌"
            color = (0, 255, 0) if max_name != 'Unknown' else (0, 0, 255)
            cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('video image', img)
    key = cv2.waitKey(10)
    if key == 27:  # ESC
        print("👋 終了します")
        break

cap.release()
cv2.destroyAllWindows()