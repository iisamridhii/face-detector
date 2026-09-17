import numpy as np
import cv2
from detector import detect_faces_and_eyes

def test_empty_frame_detection():
    """Verify that the detection pipeline executes on a blank image without errors."""
    blank_frame = np.zeros((200, 200, 3), dtype=np.uint8)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    processed_frame, count = detect_faces_and_eyes(blank_frame, face_cascade, eye_cascade)
    
    assert count == 0
    assert processed_frame.shape == (200, 200, 3)
