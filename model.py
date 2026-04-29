import os
import cv2
import numpy as np
import pickle

X = []
y = []

dataset_path = "dataset"

for category in ["clone", "inpaint", "splice"]:
    for label in ["fake", "real"]:
        folder = os.path.join(dataset_path, category, label)

        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            cap = cv2.VideoCapture(path)
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                feature = np.mean(gray)   # simple feature
                X.append([feature])
                y.append(1 if label == "fake" else 0)
            cap.release()

X = np.array(X)
y = np.array(y)


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)


with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully ")