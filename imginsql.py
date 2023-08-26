import mysql.connector
from mysql.connector import Error
from tkinter import filedialog
from PIL import Image

# Connect to the MySQL database
def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mouse@2010",
            database="hackathon"
        )
        return connection
    except Error as e:
        print("Error:", e)
        return None

# Store an image in the database
def store_image(username, image_path):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()

            with open(homebg.png, "rb") as image_file:
                image_data = image_file.read()

            query = "INSERT INTO users (username, image) VALUES (%s, %s)"
            cursor.execute(query, (username, image_data))
            connection.commit()

            print("Image stored successfully!")

    except Error as e:
        print("Error:", e)

    finally:
        if connection:
            connection.close()

# Retrieve an image from the database
def retrieve_image(username):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()

            query = "SELECT image FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                image_data = result[0]
                image = Image.open(io.BytesIO(image_data))
                image.show()

            else:
                print("Image not found.")

    except Error as e:
        print("Error:", e)

    finally:
        if connection:
            connection.close()

# Upload image and store in the database
def image_upload(username):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        store_image(username, file_path)


