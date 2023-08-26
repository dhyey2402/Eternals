import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import filedialog
import mysql.connector as con
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd


mydb = con.connect(
  host="localhost",
  user="root",
  password="mouse@2010",
  auth_plugin='mysql_native_password',
  database="result"     
)
cur = mydb.cursor()
def open_login_interface(user_type):
    global login_window
    login_window = tk.Toplevel(root)
    login_window.title(f"{user_type} Login")

    # Load background image
    bg_image = PhotoImage(file="bg1.png")

    # Create a label to hold the background image
    bg_label = tk.Label(login_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # Cover the whole window

    ttk.Label(login_window, text=f"{user_type} Login", font=("Helvetica", 30, "bold")).place(x=350, y=50)
    login_window.geometry("925x500+300+200")
    ttk.Label(login_window, text="Username:").place(x=400, y=150)
    username_entry = ttk.Entry(login_window)
    username_entry.place(x=400, y=180)

    ttk.Label(login_window, text="Password:").place(x=400, y=220)
    password_entry = ttk.Entry(login_window, show="*")
    password_entry.place(x=400, y=250)

    ttk.Button(login_window, text="Log In", command=lambda ut=user_type: login(username_entry.get(), password_entry.get())).place(x=400, y=300)

    if user_type == "Parent":
        ttk.Button(login_window, text="Sign Up", command=lambda: open_signup_interface("Parent")).place(x=400, y=350)
    else:
        ttk.Button(login_window, text="Sign Up", command=lambda: open_signup_interface("Teacher")).place(x=400, y=350)

    if user_type == "Parent":
        ttk.Button(login_window, text="Sign Up", command=lambda: open_signup_interface("Parent")).place(x=400, y=350)
    else:
        ttk.Button(login_window, text="Sign Up", command=lambda: open_signup_interface("Teacher")).place(x=400, y=350)

def image_upload(username):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        users_images[username] = file_path  # Store the image path in a dictionary

# Add a dictionary to store uploaded images
users_images = {}

def open_signup_interface(user_type):
    signup_window = tk.Toplevel(root)
    signup_window.title(f"{user_type} Sign Up")

    ttk.Label(signup_window, text=f"{user_type} Sign Up", font=("Helvetica", 14, "bold")).pack(pady=10)

    ttk.Label(signup_window, text="Username:").pack()
    username_entry_signup = ttk.Entry(signup_window)
    username_entry_signup.pack()

    ttk.Label(signup_window, text="Password:").pack()
    password_entry_signup = ttk.Entry(signup_window, show="*")
    password_entry_signup.pack(pady=5)

    # Add image upload button
    image_upload_button = ttk.Button(signup_window, text="Upload Image",command=image_upload)
    image_upload_button.pack(pady=5)

    ttk.Button(signup_window, text="Sign Up", command=lambda: signup(username_entry_signup.get(), password_entry_signup.get(), user_type)).pack(pady=10)

# Define a function to handle image upload

def signup(username, password, user_group):
    if username and password:
        if username not in users[user_group]:
            users[user_group][username] = password
            messagebox.showinfo("Success", f"{user_group[:-1].title()} account created successfully!")
        else:
            messagebox.showerror("Error", f"This {user_group[:-1]} already exists.")
    else:
        messagebox.showerror("Error", "Please provide a username and password.")


def open_communication_interface(user_type):
    interface_window = tk.Toplevel(root)
    interface_window.title(f"{user_type} Communication Interface")

def open_communication_interface(user_type):
    communication_window = tk.Toplevel(root)
    communication_window.title(f"{user_type} Communication Interface")
    
    # Create UI elements for communication (e.g., text box, send button, etc.)

    # ... (implement the communication interface here)
def image_upload():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        pil_image = Image.open(file_path)
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.config(image=tk_image)
        image_label.image = tk_image
def a():
                    newWindow7 = Toplevel(login_window)
                    newWindow7.title('Class Eighth')
                    newWindow7.geometry('925x500+300+200')
                    newWindow7.configure(bg='#fff')
                    newWindow7.resizable(False,False)
                    cur.execute("select * from eighth_final")
                    data = cur.fetchall()
                    name = []
                    for x in list(range(0, len(data))):
                        name.append(data[x][1])
                    var = StringVar(value=name)
                    listbox = Listbox(newWindow7, listvariable=var, width=30)
                    listbox.grid(row=0,column=0)
                    def update():
                        index = listbox.curselection()[0]
                        Roll_No_label2.config(text=data[index][0])
                        name_label2.config(text=data[index][1])
                        phy_label2.config(text=data[index][2])
                        chem_label2.config(text=data[index][3])
                        maths_bio_label2.config(text=data[index][4])
                        eng_label2.config(text=data[index][5])
                        cs_label2.config(text=data[index][6])
                        total_label2.config(text=data[index][7])
                        return None

                    def barplot():
                        df = pd.read_csv('Eight.csv')
                        name_data = df['Name']
                        total_data = df['Total']
                        plt.xlabel('Name')
                        plt.ylabel('Total')
                        plt.bar(name_data,total_data)
                        for i in range(len(name_data)):
                                plt.text(i, total_data[i], total_data[i], ha="center", va="bottom")
                        plt.show()

                    def pieplot():
                        df = pd.read_csv('seven.csv')
                        name_data = df["Name"]
                        total_data =  df["Total"]
                        plt.pie(total_data, labels=name_data,autopct='%1.1f%%')
                        plt.title("Class Wise Marks Distriution")
                        plt.show()

                    def lineplot():
                        df = pd.read_csv('seven.csv')
                        name_data = df["Name"]
                        total_data =  df["Total"]
                        plt.xlabel("Name")  # add label on X-axis
                        plt.ylabel("Total")  # add label on Y-axis 
                        plt.title("Class Wise Marks Distriution")
                        plt.plot(name_data,total_data,"-.")
                        plt.show()
                    
                    Roll_No_label = Label(newWindow7, text='Roll No.').grid(row=1,column=0)
                    name_label = Label(newWindow7, text='Name').grid(row=2,column=0)
                    phy_label = Label(newWindow7, text='Physics').grid(row=3,column=0)
                    chem_label = Label(newWindow7, text='Chemistry').grid(row=4,column=0)
                    maths_bio_label = Label(newWindow7, text='Maths/Biology').grid(row=5,column=0)
                    eng_label = Label(newWindow7, text='English').grid(row=6,column=0)
                    cs_label = Label(newWindow7, text='Computer Science').grid(row=7,column=0)
                    total_label = Label(newWindow7, text='Total(Out of 500)').grid(row=8,column=0)

                    Roll_No_label2 = Label(newWindow7,text="")
                    Roll_No_label2.grid(row=1,column=1,sticky="w")
                    name_label2 = Label(newWindow7, text="")
                    name_label2.grid(row=2,column=1,sticky="w")
                    phy_label2 = Label(newWindow7, text="")
                    phy_label2.grid(row=3,column=1,sticky="w")
                    chem_label2 = Label(newWindow7, text="")
                    chem_label2.grid(row=4,column=1,sticky="w")
                    maths_bio_label2 = Label(newWindow7, text="")
                    maths_bio_label2.grid(row=5,column=1,sticky="w")
                    eng_label2 = Label(newWindow7, text="")
                    eng_label2.grid(row=6,column=1,sticky="w")
                    cs_label2 = Label(newWindow7, text="")
                    cs_label2.grid(row=7,column=1,sticky="w")
                    total_label2 = Label(newWindow7, text="")
                    total_label2.grid(row=8,column=1,sticky="w")

                    btn_upd = Button(newWindow7, text="Select", command=update)
                    btn_upd.grid(row=9,column=0)
                    btn_bar_plot = Button(newWindow7, text="Click here to see Bar Graph", command=barplot)
                    btn_bar_plot.grid(row=10,column=0)
                    btn_pie_plot = Button(newWindow7, text="Click here to see Pie Chart", command=pieplot)
                    btn_pie_plot.grid(row=11,column=0)
                    btn_line_plot = Button(newWindow7, text="Click here to see Line Chart", command=lineplot)
                    btn_line_plot.grid(row=12,column=0)

def login(username, password):
    valid_users = {
        'parent1': 'password1',
        'teacher1': 'password2'
    }

    if username in valid_users and valid_users[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        a()  # Call the function here
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def main():
    global root
    root = tk.Tk()
    root.title("Parent-Teacher Communication")
    root.geometry("1104x736")  # Set window size

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), foreground="black")  # Change button text color
    style.configure("TLabel", font=("Helvetica", 14))

    # Load background imageṇ
    bg_image = PhotoImage(file="homebg.png")  # Replace with your image file

    # Create a label to hold the background image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # Cover the whole window

    label = ttk.Label(root, text="Welcome to Parent-Teacher Communication Portal", font=("Helvetica", 24, "bold"), background="#313638", foreground='white')
    label.place(x=220, y=200)

    parent_button = ttk.Button(root, text="Parent Login", style="LoginButton.TButton", command=lambda: open_login_interface("Parent"))
    parent_button.place(x=400, y=300)

    teacher_button = ttk.Button(root, text="Teacher Login", style="LoginButton.TButton", command=lambda: open_login_interface("Teacher"))
    teacher_button.place(x=400, y=400)

    style.configure("LoginButton.TButton", background="#3498db", font=("Algerian", 21))  # Change font and other styles
    style.map("LoginButton.TButton",
              background=[("active", "#2980b9")])

    root.mainloop()

if __name__ == "__main__":
    main()
