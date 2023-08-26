import tkinter as tk
from tkinter import messagebox

def sign_up():
    full_name = entry_full_name.get()
    email = entry_email.get()
    password = entry_password.get()

    # You can perform further actions here, like storing the user's data in a database.
    # For now, we'll just display a message box.
    messagebox.showinfo("Sign Up Successful", f"Welcome, {full_name}!")

# Create the main window
root = tk.Tk()
root.title("Sign Up")

# Create labels and entry fields
label_full_name = tk.Label(root, text="Full Name:")
entry_full_name = tk.Entry(root)

label_email = tk.Label(root, text="Email Address:")
entry_email = tk.Entry(root)

label_password = tk.Label(root, text="Password:")
entry_password = tk.Entry(root, show="*")

# Create the Sign Up button
sign_up_button = tk.Button(root, text="Sign Up", command=sign_up)

# Organize the widgets using the grid layout
label_full_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_full_name.grid(row=0, column=1, padx=10, pady=5)

label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_password.grid(row=2, column=1, padx=10, pady=5)

sign_up_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()

