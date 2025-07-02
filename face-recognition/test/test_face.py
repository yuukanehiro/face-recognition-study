import face_recognition

image = face_recognition.load_image_file("yuu.jpg")
face_locations = face_recognition.face_locations(image)

print(f"検出された顔の数: {len(face_locations)}")