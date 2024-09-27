from GameManager import GameManager
from RoundResult import RoundResult
from players.ComputerPlayer import ComputerPlayer
from players.HumanPlayer import HumanPlayer

computer = ComputerPlayer()
human = HumanPlayer()
game = GameManager(player1=human, player2=computer)

print("Welcome Player1!")

while True:
    result = game.play_round()

    if result == RoundResult.player1_wins:
        print("Player1 wins!")
    elif result == RoundResult.player2_wins:
        print("Player2 wins!")
    else:
        print("draw!")

    while True:
        possible_inputs = ["Y", "N"]
        user_input = input("Play again? (Y/N): ")

        if user_input.upper() not in possible_inputs:
            print(f"'{user_input}' is not a valid input!")
        else:
            break

    if user_input.upper() == "N":
        break
