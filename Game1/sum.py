import tkinter as tk
import random

# Function to generate a new question
def new_question():
    global num1, num2, answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    question_label.config(text=f"What is {num1} + {num2}?")
    entry_answer.delete(0, tk.END)

# Function to check the answer
def check_answer():
    user_answer = entry_answer.get()
    if user_answer.isdigit() and int(user_answer) == answer:
        result_label.config(text="Correct! 🎉", fg="green")
    else:
        result_label.config(text=f"Wrong! ❌ Correct answer: {answer}", fg="red")
    new_question()

# Tkinter Window
root = tk.Tk()
root.title("Math Game")
root.geometry("300x200")

question_label = tk.Label(root, text="", font=("Arial", 14))
question_