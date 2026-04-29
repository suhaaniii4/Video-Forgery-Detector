import cv2
import numpy as np

class VideoForgeryDetector:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def extract_frames(self, sampling_rate=2):
        frames = []
        for i in range(self.total_frames):
            ret, frame = self.cap.read()
            if not ret:
                break
            if i % sampling_rate == 0:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frames.append(gray)
        self.cap.release()
        return frames

    def calculate_mse(self, f1, f2):
        return np.mean((f1.astype("float") - f2.astype("float")) ** 2)

    def analyze(self, frames):
        sims = []
        for i in range(1, len(frames)):
            sims.append(self.calculate_mse(frames[i-1], frames[i]))
        return sims

    def detect(self, sims):
        mean = np.mean(sims)
        std = np.std(sims)

        suspicious = []
        for i, val in enumerate(sims):
            if val > mean + 0.8 * std:
                suspicious.append(i)
        return suspicious


def simple_detection(video_path):
    detector = VideoForgeryDetector(video_path)
    frames = detector.extract_frames()
    sims = detector.analyze(frames)
    suspicious = detector.detect(sims)

    results = {
        "similarities": sims,
        "combined_suspicious": suspicious,
        "total_frames_analyzed": len(frames)
    }

    return detector, results