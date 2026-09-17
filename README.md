# Real-Time Face & Eye Detector - VITyarthi Project

**Name:** Samridhi Shree  
**Registration No:** 24BAI10161  
**Course:** Computer Vision  

---

## 1. Project Overview
This project is a lightweight, real-time computer vision system built using Python and OpenCV. It captures a live webcam video feed and applies pre-trained Haar Cascade classifiers to identify and annotate human faces and eyes frame-by-frame with bounding boxes and an on-screen face counter.

---

## 2. Repository Architecture & File Structure
The project is organized in a modular structure to maintain code readability and separation of concerns:

```text
simple-face-detector/
│
├── config.py           # Configuration constants (scaling, minimum neighbors)
├── detector.py         # Core OpenCV face and eye detection processing logic
├── main.py             # Application entry point (webcam loop and rendering)
├── test_detector.py    # Automated unit test suite run via Pytest
├── statement.md        # Detailed academic problem statement documentation
└── README.md           # Project documentation and quickstart guide
