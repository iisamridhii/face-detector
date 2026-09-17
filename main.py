import cv2
from detector import detect_faces_and_eyes

def main():
    # Load pre-trained OpenCV Haar Cascade classifiers
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)
    print("Starting webcam feed... Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab camera frame.")
            break
            
        processed_frame, face_count = detect_faces_and_eyes(frame, face_cascade, eye_cascade)
        
        # Display detection overlay text
        cv2.putText(processed_frame, f"Faces Detected: {face_count}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        cv2.imshow("Face & Eye Detector", processed_frame)
        
        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
