import random as r

player_wins = 0
computer_wins = 0
total = 0
draws = 0

options = ["Rock", "Paper", "Scissors"]
quit_game = "q"

computer_pick = r.choice(options)

playing = True

while playing:
    player_pick = input("Enter an option: ").capitalize()
    if player_pick == "Q":
        break

    elif player_pick not in options:
        continue

    if player_pick == "Rock" and computer_pick == "Scissors":
        print(f"Computer picked: {computer_pick}")
        print("You win!")
        player_wins += 1
        total += 1
        draws += 1

    elif player_pick == "Paper" and computer_pick == "Rock":
        print(f"Computer picked: {computer_pick}")
        print("You win!")
        player_wins += 1
        total += 1
        draws += 1

    elif player_pick == "Scissors" and computer_pick == "Paper":
        print(f"Computer picked: {computer_pick}")
        print("You win!")
        player_wins += 1
        total += 1
        draws += 1

    elif player_pick == computer_pick:
        print(f"Computer picked: {computer_pick}")
        print("Draw!")
        total += 1
        draws += 1

    else:
        print(f"Computer picked: {computer_pick}")
        print("You lost!")
        computer_wins += 1
        total += 1
        draws += 1
    computer_pick = r.choice(options)

print(
    "You played",
    total,
    "games. Won:",
    player_wins,
    "| Lost: ",
    computer_wins,
    "| Draws: ",
    draws,
)
print("Goodbye!")
