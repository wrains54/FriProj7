import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to authenticate user login
def sign_in():
    email = email_login_entry.get()
    password = password_login_entry.get()

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    # Check if the email and password match in the database
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    if c.fetchone() is not None:
        success_label.config(text="Login successful", fg="green")
        # Clear all input fields upon successful login
        clear_fields()
    else:
        error_label.config(text="Email or password incorrect. Please try again.", fg="red")
        # Clear only the password field if the login fails
        password_login_entry.delete(0, tk.END)

    conn.close()

# Function to clear all input fields
def clear_fields():
    email_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)

# Create the sign-in window
def signin_window():
    root = tk.Tk()
    root.title("Sign In")

    tk.Label(root, text="Email:").pack()
    global email_login_entry
    email_login_entry = tk.Entry(root)
    email_login_entry.pack()

    tk.Label(root, text="Password:").pack()
    global password_login_entry
    password_login_entry = tk.Entry(root, show="*")
    password_login_entry.pack()

    global error_label
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()

    global success_label
    success_label = tk.Label(root, text="", fg="green")
    success_label.pack()

    signin_button = tk.Button(root, text="Sign In", command=sign_in)
    signin_button.pack()

    root.mainloop()

if __name__ == "__main__":
    signin_window()