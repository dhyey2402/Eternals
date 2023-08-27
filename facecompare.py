import face_recognition

# Load the reference image
reference_image = face_recognition.load_image_file("reference_image.jpg")
reference_embedding = face_recognition.face_encodings(reference_image)[0]

# Capture a frame from the camera
frame = cv2.imread("recognized_face.jpg")
recognized_embedding = face_recognition.face_encodings(frame)[0]

# Calculate the Euclidean distance between embeddings
distance = face_recognition.face_distance([reference_embedding], recognized_embedding)

# Define a threshold
threshold = 0.6

# Compare distances and determine match
if distance < threshold:
    print("Face matches!")
else:
    print("Face does not match.")
