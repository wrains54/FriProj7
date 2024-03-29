import tkinter as tk
from tkinter import messagebox
import re
import sqlite3

# Function to validate email format
def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return pattern.match(email)

# Function to create a new user account
def create_account(event=None):
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Clear previous error messages
    clear_messages()

    # Check if any field is empty
    if not name or not email or not password or not confirm_password:
        error_label.config(text="Enter All Required Inforamtion", fg="red")
        return

    # Validate email format
    if not validate_email(email):
        error_label.config(text="Please enter a valid email address", fg="red")
        return

    # Validate password match
    if password != confirm_password:
        error_label.config(text="Passwords do not match", fg="red")
        return

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    # Create the "users" table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 email TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL)''')

    # Check if the email already exists in the database
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    if c.fetchone() is not None:
        error_label.config(text="Email already exists", fg="red")
        conn.close()
        return

    # Insert new user into the database
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

    signup_button = tk.Button(root, text="Create Account", command=create_account)
    signup_button.pack()

    # Bind Enter key press event to sign-up button
    root.bind("<Return>", create_account)

    root.mainloop()

if __name__ == "__main__":
    signup_window()