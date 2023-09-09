import tkinter as tk
from tkinter import messagebox
import mysql.connector


def save_student_data():
    name = name_entry.get()
    student_class = class_entry.get()
    english_mark = int(english_entry.get())
    tamil_mark = int(tamil_entry.get())
    maths_mark = int(maths_entry.get())
    science_mark = int(science_entry.get())
    social_mark = int(social_entry.get())
    total_mark = english_mark + tamil_mark + maths_mark + science_mark + social_mark

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="ramya",
            password="ramya",
            database="test"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            insert_query = "INSERT INTO data (name, class, english_mark, tamil_mark, maths_mark, science_mark, social_mark, total_mark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (name, student_class, english_mark, tamil_mark, maths_mark, science_mark, social_mark, total_mark)
            cursor.execute(insert_query, data)
            conn.commit()
            messagebox.showinfo("Success", "Student data saved successfully")

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", "Error connecting to MySQL database: " + str(e))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def open_student_details_window(username):
    global current_username
    current_username = username

    login_window.destroy()
    student_window = tk.Tk()
    student_window.title("Student Data Entry")
    name_label = tk.Label(student_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(student_window)
    name_entry.pack()
    class_label = tk.Label(student_window, text="Class:")
    class_label.pack()
    class_entry = tk.Entry(student_window)
    class_entry.pack()
    english_label = tk.Label(student_window, text="English Mark:")
    english_label.pack()
    english_entry = tk.Entry(student_window)
    english_entry.pack()
    tamil_label = tk.Label(student_window, text="Tamil Mark:")
    tamil_label.pack()
    tamil_entry = tk.Entry(student_window)
    tamil_entry.pack()
    maths_label = tk.Label(student_window, text="Maths Mark:")
    maths_label.pack()
    maths_entry = tk.Entry(student_window)
    maths_entry.pack()
    science_label = tk.Label(student_window, text="Science Mark:")
    science_label.pack()
    science_entry = tk.Entry(student_window)
    science_entry.pack()
    social_label = tk.Label(student_window, text="Social Mark:")
    social_label.pack()
    social_entry = tk.Entry(student_window)
    social_entry.pack()
    save_button = tk.Button(student_window, text="Save Student Data", command=save_student_data)
    save_button.pack()
    student_window.mainloop()


login_window = tk.Tk()
login_window.title("Login")
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="ramya",
            password="ramya",
            database="register"
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Login Successful", "Welcome, " + user[0])  
                open_student_details_window(username)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", "Error connecting to MySQL database: " + str(e))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()
login_window.mainloop()
