import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_data.csv")

# Features & target
X = data[['study_hours', 'attendance', 'sleep_hours']]
y = data['marks']

# Train model
model = LinearRegression()
model.fit(X, y)

# Function for prediction
def predict_marks():
    try:
        study = float(entry_study.get())
        attendance = float(entry_attendance.get())
        sleep = float(entry_sleep.get())

        result = model.predict([[study, attendance, sleep]])
        marks = round(result[0], 2)

        output = f"Predicted Marks: {marks}\n"

        # Suggestions
        if marks < 50:
            output += "Suggestion: Increase study time & attendance."
        elif marks < 75:
            output += "Suggestion: You are doing okay, improve consistency."
        else:
            output += "Excellent! Keep it up."

        label_result.config(text=output)

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Function to show graph
def show_graph():
    plt.scatter(data['study_hours'], data['marks'])
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.title("Study Hours vs Marks")
    plt.show()

# GUI Window
root = tk.Tk()
root.title("Student Performance Predictor")
root.geometry("400x400")

# Title
tk.Label(root, text="Student Performance Predictor", font=("Arial", 14)).pack(pady=10)

# Inputs
tk.Label(root, text="Study Hours").pack()
entry_study = tk.Entry(root)
entry_study.pack()

tk.Label(root, text="Attendance (%)").pack()
entry_attendance = tk.Entry(root)
entry_attendance.pack()

tk.Label(root, text="Sleep Hours").pack()
entry_sleep = tk.Entry(root)
entry_sleep.pack()

# Buttons
tk.Button(root, text="Predict Marks", command=predict_marks, bg="lightblue").pack(pady=10)
tk.Button(root, text="Show Graph", command=show_graph, bg="lightgreen").pack(pady=5)

# Result
label_result = tk.Label(root, text="", wraplength=300)
label_result.pack(pady=10)

# Run app
root.mainloop()