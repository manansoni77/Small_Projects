import os
import pickle
import cv2
import face_recognition
from face_recognition.api import face_encodings
import numpy as np

feature_vectors = {}
final_features = {}
path = "./"

dirs = [i for i in os.listdir() if os.path.isdir(i)]

for dir in dirs:
    feature_vectors[dir] = []
    path2 = path+dir+"/"
    for file in os.listdir(path2):
        bgr = cv2.imread(path2+file)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        box = face_recognition.face_locations(rgb)
        encoding = face_recognition.face_encodings(rgb,box)[0]
        feature_vectors[dir].append(encoding)
        break

for key in feature_vectors:
    vectors = feature_vectors[key]
    sum_vectors = np.zeros(128)
    for vector in vectors:
        sum_vectors = np.add(sum_vectors, vector)
    avg_vectors = sum_vectors/(len(vectors))
    final_features[key] = avg_vectors

# print(final_features)

with open('features.txt','wb') as fp:
    pickle.dump(final_features, fp)
