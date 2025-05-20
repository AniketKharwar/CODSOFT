import tkinter as tk
import random

user_score = 0
computer_score = 0

def determine_winner(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    label_result.config(text=f"Computer chose: {computer_choice}\n{result}")
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def play_again():
    label_result.config(text="Choose your move!")
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack()

label_result = tk.Label(root, text="Choose your move!", font=("Arial", 12))
label_result.pack()

label_score = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}", font=("Arial", 12))
label_score.pack()

btn_rock = tk.Button(frame, text="Rock", command=lambda: determine_winner("rock"))
btn_rock.pack(side=tk.LEFT, padx=5)

btn_paper = tk.Button(frame, text="Paper", command=lambda: determine_winner("paper"))
btn_paper.pack(side=tk.LEFT, padx=5)

btn_scissors = tk.Button(frame, text="Scissors", command=lambda: determine_winner("scissors"))
btn_scissors.pack(side=tk.LEFT, padx=5)

btn_play_again = tk.Button(root, text="Play Again", command=play_again)
btn_play_again.pack(pady=10)

root.mainloop()