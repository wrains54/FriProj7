import tkinter as tk
from tkinter import messagebox
import re
import sqlite3


conn = sqlite3.connect('user_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 email TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL)''')


c.execute("SELECT * FROM users WHERE email=?", (email,))
if c.fetchone() is not None:
    error_label.config(text="Email already exists", fg="red")
    conn.close()
  
