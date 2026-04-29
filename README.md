# Video-Forgery-Detector
“A Flask-based Video Forgery Detection System that analyzes frame-level differences using MSE, SSIM, and ML techniques to detect tampered videos with visual graphs and performance metrics.”
#Video Forgery Detection System

This project is a Flask-based web application that detects whether a video is tampered or not using frame-level analysis and machine learning techniques.

---

##Features

- Upload and analyze video files
- Detect tampered frames using MSE & SSIM
- Highlight suspicious frames
- Display:
  - Accuracy
  - Forgery Type (Clone, Splice, Inpaint)
  - Precision, Recall, F1 Score
  - ROC Curve & AUC Score
  - Precision-Recall Curve
- Visual graphs using Matplotlib

---

##Technology Used

- Python
- Flask
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn

---

#How It Works

1. Video is uploaded via web interface  
2. Frames are extracted using OpenCV  
3. Frame differences are calculated (MSE & SSIM)  
4. Suspicious frames are detected using statistical thresholds  
5. Tampering ratio is computed  
6. Final result is predicted  
7. Graphs and metrics are generated  

---

## Project Structure
project/
│── app.py
│── detector.py
│── templates/
│── static/
│── uploads/
