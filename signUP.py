import tkinter as tk
from tkinter import messagebox
import re
import sqlite3


def sign_in():
    email = email_login_entry.get()
    password = password_login_entry.get()

    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    if c.fetchone() is not None:
        success_label.config(text="Login successful", fg="green")
        clear_fields()
    else:
        error_label.config(text="Email or password incorrect.", fg="red")
        password_login_entry.delete(0, tk.END)

    conn.close()

def clear_fields():
    email_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)

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

    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()

    # Display success message
    success_label.config(text="Account Created", fg="green")

    # Clear input fields
    clear_fields()

# Function to clear error and success messages
def clear_messages():
    error_label.config(text="")
    success_label.config(text="")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Create the sign-up window
def signup_window():
    root = tk.Tk()
    root.title("Sign Up")

    tk.Label(root, text="Name:").pack()
    global name_entry
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Email:").pack()
    global email_entry
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Password:").pack()
    global password_entry
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Label(root, text="Retype Password:").pack()
    global confirm_password_entry
    confirm_password_entry = tk.Entry(root, show="*")
    confirm_password_entry.pack()

    global error_label
    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()

    global success_label
    success_label = tk.Label(root, text="", fg="green")
    success_label.pack()

    signup_button = tk.Button(root, text="Sign Up", command=create_account)
    signup_button.pack()

    # Bind Enter key press event to sign-up button
    root.bind("<Return>", create_account)

    root.mainloop()

if __name__ == "__main__":
    signup_window()