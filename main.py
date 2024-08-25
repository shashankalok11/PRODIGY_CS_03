import tkinter as tk
from tkinter import messagebox
import re

# Function to check the password strength
def check_password_strength(password):
    # Criteria initialization
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None  # \W matches any non-alphanumeric character

    # Strength score calculation
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Feedback messages
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    # Strength evaluation
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Function to be called when the button is clicked
def on_check_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    
    result_label.config(text=f"Password Strength: {strength}")
    
    if feedback:
        feedback_text = "\n".join(feedback)
        feedback_label.config(text=f"Feedback:\n{feedback_text}")
    else:
        feedback_label.config(text="")

# Setting up the GUI
root = tk.Tk()
root.title("Password Strength Checker")

# Create widgets
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=on_check_password)
check_button.pack(pady=10)

result_label = tk.Label(root, text="Password Strength: ")
result_label.pack(pady=10)

feedback_label = tk.Label(root, text="", justify="left")
feedback_label.pack(pady=10)

# Run the application
root.mainloop()
