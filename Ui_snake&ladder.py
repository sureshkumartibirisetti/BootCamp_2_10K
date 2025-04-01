import tkinter as tk
import random
import time

# Game variables
a = 0
b = 0
a_s = 0
b_s = 0
ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 86: 99}
snakes = {32: 10, 36: 6, 48: 26, 63: 18, 88: 24, 95: 56, 97: 78}
turn = "Player 1"

# UI Setup
root = tk.Tk()
root.title("Snake and Ladder Game")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Snake & Ladder!", font=("Arial", 14))
label.pack(pady=10)

turn_label = tk.Label(root, text=f"Turn: {turn}", font=("Arial", 12))
turn_label.pack()

player1_label = tk.Label(root, text=f"Player 1 Position: {a}", font=("Arial", 12))
player1_label.pack()

player2_label = tk.Label(root, text=f"Player 2 Position: {b}", font=("Arial", 12))
player2_label.pack()

dice_label = tk.Label(root, text="Roll the dice!", font=("Arial", 12))
dice_label.pack()

def roll_dice():
    global a, b, a_s, b_s, turn
    dice_value = random.randint(1, 6)
    dice_label.config(text=f"Dice: {dice_value}")
    
    if turn == "Player 1":
        if a_s == 0 and dice_value in [1, 6]:
            a_s = 1
        if a_s == 1:
            a += dice_value
            if a in ladder:
                a = ladder[a]
            elif a in snakes:
                a = snakes[a]
            if a >= 100:
                label.config(text="🎉 Player 1 Wins! 🎉")
                return
        turn = "Player 2"
    
    else:
        if b_s == 0 and dice_value in [1, 6]:
            b_s = 1
        if b_s == 1:
            b += dice_value
            if b in ladder:
                b = ladder[b]
            elif b in snakes:
                b = snakes[b]
            if b >= 100:
                label.config(text="🎉 Player 2 Wins! 🎉")
                return
        turn = "Player 1"
    
    turn_label.config(text=f"Turn: {turn}")
    player1_label.config(text=f"Player 1 Position: {a}")
    player2_label.config(text=f"Player 2 Position: {b}")

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 12))
roll_button.pack(pady=20)

root.mainloop()
