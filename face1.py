import cv2
import tkinter as tk
from tkinter import filedialog

# Function to capture and save an image
def capture_image(save_directory, filename):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Captured Image", frame)
        cv2.imwrite(f"{save_directory}/{filename}.jpg", frame)
        print("Image saved successfully!")
    else:
        print("Failed to capture image.")

# Create the main GUI window
root = tk.Tk()
root.title("Image Capture")
root.configure(bg="#212122")
root.geometry("925x500+300+200")

# Initialize camera
cap = cv2.VideoCapture(0)

# Function to open a file dialog and set the save directory
def set_save_directory():
    global save_directory
    save_directory = filedialog.askdirectory()

# Create UI elements
set_directory_button = tk.Button(root, text="Set Save Directory",font=("Modern",15,"bold"), command=set_save_directory)
set_directory_button.place(x=390.5,y=100)

filename_label = tk.Label(root,font=("Modern",15,"bold"), text="Enter Filename:")
filename_label.place(x=401,y=150)

filename_entry = tk.Entry(root,font=("Modern",15,"bold"))
filename_entry.place(x=380,y=200)

capture_button = tk.Button(root, text="Capture Image",font=("Modern",15,"bold"), command=lambda: capture_image(save_directory, filename_entry.get()))
capture_button.place(x=400,y=250)

# Start the main event loop
root.mainloop()

# Release camera when the application is closed
cap.release()
cv2.destroyAllWindows()
