import cv2
import pickle
import face_recognition
import numpy as np

vid = cv2.VideoCapture(0)
captured_images = []
name_features = {}

def get_encoding(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb,boxes)
    return boxes,encodings

while True:
    ret, frame = vid.read()
    if not ret:
        print("Could not grab image")
        break
    cv2.imshow('Image',frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        vid.release()
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print("Capturing image")
        captured_images.append(frame)

cv2.destroyAllWindows()

for img in captured_images:
    boxes,encodings = get_encoding(img)
    for i,box in enumerate(boxes):
        t,r,b,l = box
        crop = img[t:b,l:r]
        cv2.imshow('person',crop)
        cv2.waitKey(2)
        name = input("Enter name of person - ")
        if name in name_features:
            name_features[name] = np.add(name_features[name],encodings[i])
        else:
            name_features[name] = encodings[i]

print(name_features)

with open('features_vid.txt','wb') as fp:
    pickle.dump(name_features, fp)