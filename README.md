#🎓 Student Performance Prediction System

Hey there! 👋
This project is a simple yet powerful **Machine Learning application** that predicts student marks based on daily habits.

It uses three key factors:

* 📚 Study Hours
* 👨‍🎓 Attendance
* 😴 Sleep Hours

`` 🚀 What This Project Does

This system takes basic student input and:

✅ Predicts marks using **Linear Regression (ML model)**
✅ Provides **personalized suggestions** to improve performance
✅ Displays a **graph** showing the relationship between study hours and marks
✅ Offers a **user-friendly GUI** built with Tkinter


 ``🧠 Machine Learning Concept Used

* Algorithm: **Linear Regression**
* Type: **Supervised Learning**
* Goal: Predict continuous values (marks)

`` 📂 Project Structure

Your folder should contain:


student_performance_predictor/
│
├── student_predictor.py   # Main application (GUI + ML model)
├── student_data.csv       # Dataset (training data)
└── README.md              # Project documentation


---

``📊 Dataset Format

Your CSV file must follow this format:


study_hours,attendance,sleep_hours,marks
2,60,5,45
3,65,6,50
4,70,6,55
5,75,7,65
6,80,7,70
7,85,7,78
8,90,8,85
1,50,4,35
9,95,8,90

---

``⚙️ Installation & Running the Project

 1. Install required libraries
   pip install pandas scikit-learn matplotlib


 2. Run the application
 python student_predictor.py

``🖥️ How to Use the Application

   1. Run the program → GUI window will open

   2. Enter:

   * Study Hours
   * Attendance (%)
   * Sleep Hours

   3. Click **"Predict Marks"**

   4. Get instant output:

   * 🎯 Predicted marks
   * 💡 Improvement suggestions

`` 📌 Example

**Input:**

* Study Hours: 6
* Attendance: 80%
* Sleep: 7 hours

**Output:**

Predicted Marks: 72.5  
Suggestion: You are doing well, try to maintain consistency.

`` 📈 Features

* ✔ Real-time prediction
* ✔ Simple and clean GUI
* ✔ Graph visualization
* ✔ Suggestion system
* ✔ Easy to understand & use



`` 🌍 Real-World Application

This system can be used in:

* Schools and colleges
* Student performance analysis
* Personalized learning systems



``🎯 Project Objective

To demonstrate how **Machine Learning can be applied to real-life problems** by analyzing student habits and predicting academic performance.



`` 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Tkinter


``❗ Important Notes

* Ensure `student_data.csv` is in the **same folder** as the Python file
* Enter only **numeric values** in input fields
* Dataset quality affects prediction accuracy


``🤝 Need Help?

If you face any issues:

* Check file paths
* Verify dataset format
* Ensure libraries are installed

Or simply raise an issue on GitHub 😊


``⭐ Final Note

This project is designed to be:

* Simple ✔
* Practical ✔
* Easy to understand ✔

Perfect for demonstrating **AI & ML fundamentals in a real-world scenario**.

# Author : Ishant Kumar Sahu

🚀 Made with curiosity and learning spirit!
