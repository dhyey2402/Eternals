import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        pil_image = Image.open(file_path)
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.config(image=tk_image)
        image_label.image = tk_image

def main():
    root = tk.Tk()
    root.title("Image Upload")

    select_button = ttk.Button(root, text="Select Image", command=open_image)
    select_button.pack()

    global image_label
    image_label = tk.Label(root)
    image_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
