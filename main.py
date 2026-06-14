import random

# Score
player_score = 0
computer_score = 0


moves = ["Rock", "Paper", "Scissors"]


# AI prediction (basic learning logic)
history = []


def ai_move():
    if len(history) < 3:
        return random.choice(moves)

    # Predict user's most used move
    prediction = max(
        set(history),
        key=history.count
    )

    # AI chooses winning move
    if prediction == "Rock":
        return "Paper"

    elif prediction == "Paper":
        return "Scissors"

    else:
        return "Rock"



def check_winner(player, computer):

    global player_score, computer_score

    if player == computer:
        return "Draw"

    elif (
        (player=="Rock" and computer=="Scissors") or
        (player=="Paper" and computer=="Rock") or
        (player=="Scissors" and computer=="Paper")
    ):
        player_score += 1
        return "You Win ??"

    else:
        computer_score += 1
        return "Computer Wins ??"



print("AI Rock Paper Scissors Game")
print("Type Rock / Paper / Scissors")
print("Type exit to quit")


while True:

    player = input("\nYour move: ").capitalize()


    if player == "Exit":
        break


    if player not in moves:
        print("Invalid choice!")
        continue


    history.append(player)


    computer = ai_move()


    result = check_winner(
        player,
        computer
    )


    print("Computer move:", computer)
    print(result)

    print(
        "Score --> You:",
        player_score,
        "Computer:",
        computer_score
    )


print("\nFinal Score")
print("You:", player_score)
print("Computer:", computer_score)
print("Thanks for playing!")
