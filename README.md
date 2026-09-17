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
```
## 3. Prerequisites & Installation
Step 1: Install Python
Ensure Python 3.10 or newer is installed on your system. Verify your installation by running:

```text
Bash

python --version
```
Step-2: Install Dependencies
Open your terminal in VS Code (Ctrl + ~) and install the required libraries:

```text
Bash

pip install opencv-python numpy pytest
```
## 4. Usage Instructions
Running the Application
Launch the live face detection system by running:

```text
Bash

python main.py
```
Face Box: Blue rectangle

Eye Box: Green rectangle

Exit: Press the q key while focused on the video window to stop the program.

Running Unit Tests
To verify that the detection function processes frame arrays correctly, execute:

```text
Bash

python -m pytest
```
## 5. Implementation Summary

Haar Cascades: Uses haarcascade_frontalface_default.xml and haarcascade_eye.xml provided natively by OpenCV.

Testing Framework: Leverages pytest using synthetic matrix arrays generated with numpy to validate detector pipeline outputs without needing a live hardware camera during test runs.

## 6. Future Enhancements & Contributions

Deep Learning Integration: Upgrade detection modules to DNN or MediaPipe models for higher accuracy under low-light conditions.

FPS Optimization: Implement multi-threading for frame capturing to improve frame rates on lower-end hardware.

Emotion & Landmark Tracking: Extend detection beyond faces and eyes to identify facial landmarks and basic expressions.







