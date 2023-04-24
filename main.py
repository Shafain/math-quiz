import random
import tkinter as tk

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print("Invalid operator")
        return None

def check_guess():
    guess = int(guess_entry.get())
    if guess == result:
        result_label.config(text="Congratulations! You guessed the correct answer.")
    else:
        result_label.config(text=f"Sorry, the correct answer was {result}. Better luck next time!")

def play_game():
    global num1, num2, operator, result
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    result = calculate(num1, num2, operator)

    question_label.config(text=f"The calculator displays: {num1} {operator} {num2} = ?")
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Number Guessing Game")

question_label = tk.Label(window, text="")
question_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

check_button = tk.Button(window, text="Check Guess", command=check_guess)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

play_button = tk.Button(window, text="Play Again", command=play_game)
play_button.pack()

play_game()

window.mainloop()
