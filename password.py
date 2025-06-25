import re
import tkinter as tk
from tkinter import messagebox
import random
import string

try:
    from nltk.corpus import words
    nltk_installed = True
    word_list = set(words.words())
except:
    nltk_installed = False
    word_list = set()

def check_password_strength(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short (min 8 characters).")
    if not re.search(r"[A-Z]", password):
        feedback.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("Add at least one lowercase letter.")
    if not re.search(r"\d", password):
        feedback.append("Include at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Add special characters (e.g., !, @, #).")
    if nltk_installed and password.lower() in word_list:
        feedback.append("Avoid using dictionary words.")

    if not feedback:
        return "Strong password!", []
    else:
        return "Weak password!", feedback

def suggest_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(12))

def analyze_password():
    pwd = entry.get()
    strength, feedback = check_password_strength(pwd)
    result_label.config(text=strength, fg="green" if strength == "Strong password!" else "red")
    
    suggestions_box.delete("1.0", tk.END)
    if feedback:
        for f in feedback:
            suggestions_box.insert(tk.END, f + "\n")
        suggestions_box.insert(tk.END, f"\nSuggestion: Try something like '{suggest_password()}'")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x350")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Helvetica", 14)).pack(pady=10)
entry = tk.Entry(root, show="*", font=("Helvetica", 14), width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", font=("Helvetica", 12), command=analyze_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

tk.Label(root, text="Feedback / Suggestions:", font=("Helvetica", 12)).pack(pady=5)
suggestions_box = tk.Text(root, height=8, width=50, font=("Helvetica", 10))
suggestions_box.pack()

root.mainloop()
