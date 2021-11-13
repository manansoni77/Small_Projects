import cv2
import pickle
import face_recognition
from face_recognition.api import face_locations
import numpy as np

with open('features_vid.txt','rb') as fp:
    features = pickle.load(fp)

vid = cv2.VideoCapture(0)
captured_images = []

while True:
    ret, frame = vid.read()
    if not ret:
        print("Could not grab image")
        break
    cv2.imshow('Image',frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print("Capturing image")
        captured_images.append(frame)

# frame = cv2.imread("test.png")
# print(frame.shape)
# captured_images.append(frame)

for img in captured_images:
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    print(boxes)
    encodings = face_recognition.face_encodings(rgb,boxes)
    names = []
    for encoding in encodings:
        dist = 100
        name = ''
        for key in features:
            ndist = np.linalg.norm(features[key]-encoding)
            print(key,ndist)
            if ndist<dist:
                dist = ndist
                name = key
        names.append(name)
    for i,box in enumerate(boxes):
        # x,y,w,h = box
        # cv2.rectangle(img,(x,y-h),(x+w,y),(0,0,0))
        # cv2.putText(img, names[i], (x,y-h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
        t,r,b,l = box
        cv2.rectangle(img,(l,t),(r,b),(0,0,0))
        cv2.putText(img, names[i], (l,t), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
    cv2.imshow('image',img)
    cv2.waitKey(0)