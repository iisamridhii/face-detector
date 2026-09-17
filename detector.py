import cv2

def detect_faces_and_eyes(frame, face_cascade, eye_cascade):
    """Detects faces and eyes in a given video frame and draws bounding boxes."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    face_count = len(faces)
    
    for (x, y, w, h) in faces:
        # Draw blue box around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Region of interest for eyes inside the face box
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Draw green box around eyes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            
    return frame, face_count
