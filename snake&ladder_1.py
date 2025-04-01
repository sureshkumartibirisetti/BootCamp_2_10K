import random
import time

a = 0
b = 0
a_s = 0
b_s = 0

ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 86: 99}
snakes = {32: 10, 36: 6, 48: 26, 63: 18, 88: 24, 95: 56, 97: 78}

while a < 100 and b < 100:
    # Player 1's turn
    x = random.randint(1, 6)
    if a_s == 0 and (x == 1 or x == 6):  
        a_s = 1  # Allow Player 1 to start moving

    if a_s == 1:
        a += x
        if a in ladder:
            a = ladder[a]
        elif a in snakes:
            a = snakes[a]

        if a < 100 and x == 6:
            x = random.randint(1, 6)
            a += x
            if a in ladder:
                a = ladder[a]
            elif a in snakes:
                a = snakes[a]
            if x == 6:
                a -= x  # Reset move if three sixes are rolled

        if a >= 100:
            time.sleep(5)  # Wait before showing the winner
            print("🎉 Player 1 wins the game! 🎉")
            break

    # Player 2's turn
    y = random.randint(1, 6)
    if b_s == 0 and (y == 1 or y == 6):  
        b_s = 1  # Allow Player 2 to start moving

    if b_s == 1:
        b += y
        if b in ladder:
            b = ladder[b]
        elif b in snakes:
            b = snakes[b]

        if b < 100 and y == 6:
            y = random.randint(1, 6)
            b += y
            if b in ladder:
                b = ladder[b]
            elif b in snakes:
                b = snakes[b]
            if y == 6:
                b -= y  # Reset move if three sixes are rolled

        if b >= 100:
            time.sleep(5)  # Wait before showing the winner
            print("🎉 Player 2 wins the game! 🎉")
            break
