import cv2
import pickle
import face_recognition
from face_recognition.api import face_locations
import numpy as np
import video

with open('features.txt','rb') as fp:
    features = pickle.load(fp)

def process(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb,boxes)
    names = []
    for encoding in encodings:
        dist = 100
        name = ''
        for key in features:
            ndist = np.linalg.norm(features[key]-encoding)
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
    return img

cam = video.Vidget(0).start()

while True:
    if cam.stop:
        print("Could not grab image")
        break
    frame = cam.frame
    frame = process(frame)
    cv2.imshow('Image',frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        cam.stop = True
        print("Escape hit, closing...")
        break
