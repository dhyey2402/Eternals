import cv2
import numpy as np

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(r'C:\Users\dhyey\OneDrive\Documents\Hackathon\haarcascade_frontalface_default.xml') 

# Load a pre-trained deep learning model for face recognition (you can replace this with your own model)
# Here, we're using a simple NumPy array as a placeholder for face embeddings
known_faces = {
    "person_1": np.random.rand(128),  # Replace with actual face embeddings
    "person_2": np.random.rand(128),
    # Add more known faces and their embeddings
}

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        
        # Resize the face ROI for face recognition model (assuming it requires a specific input size)
        resized_face = cv2.resize(face_roi, (128, 128))
        
        # Placeholder for face recognition result
        detected_face_embedding = np.random.rand(128)  # Replace with actual face recognition output
        
        # Compare the detected face embedding with known faces
        found_match = False
        for name, known_embedding in known_faces.items():
            similarity = np.dot(known_embedding, detected_face_embedding) / (np.linalg.norm(known_embedding) * np.linalg.norm(detected_face_embedding))
            
            if similarity > 0.6:  # Adjust this threshold
                cv2.putText(frame, f"Match: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                found_match = True
                break
        
        if not found_match:
            cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow("Face Recognition", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
