import tkinter as tk

def check_answer(question, correct_answer):
    user_answer = entry.get().strip().lower()
    if user_answer == correct_answer.lower():
        result_label.config(text="Correct!")
        update_score()
    else:
        result_label.config(text="Incorrect!")

def update_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

def next_question():
    global current_question_index
    if current_question_index < len(questions):
        question_label.config(text=questions[current_question_index])
        current_question_index += 1
        entry.delete(0, tk.END)
        result_label.config(text="")
    else:
        end_quiz()

def end_quiz():
    result_label.config(text=f"End of Quiz\nYou got {score} questions correct\nYour score is {score / len(questions) * 100}%")
    next_button.config(state=tk.DISABLED)

# Questions and Answers
questions = [
    "What is the capital city of Spain?",
    "What is the capital city of France?",
    "What is the capital city of Germany?",
    "What is the capital city of Italy?",
    "What is the capital city of The Netherlands?"
]
answers = ["Madrid", "Paris", "Berlin", "Rome", "Amsterdam"]

# Initialize variables
current_question_index = 0
score = 0

# Create the main window
window = tk.Tk()
window.title("Capital City Quiz Game")

# Create widgets
question_label = tk.Label(window, text=questions[current_question_index])
question_label.pack(pady=10)

entry = tk.Entry(window, width=20)
entry.pack(pady=10)

check_button = tk.Button(window, text="Check Answer", command=lambda: check_answer(questions[current_question_index], answers[current_question_index]))
check_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score: 0")
score_label.pack(pady=10)

next_button = tk.Button(window, text="Next Question", command=next_question)
next_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
