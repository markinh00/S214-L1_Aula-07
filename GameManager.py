from Choice import Choice
from RoundResult import RoundResult
from players.Player import Player


class GameManager:
    def __init__(self, player1: Player, player2: Player):
        self.player1: Player = player1
        self.player2: Player = player2

    def play_round(self) -> RoundResult:
        p1_choice = self.player1.get_choice()
        p2_choice = self.player2.get_choice()

        print(f"Player1 picked '{p1_choice.value}' and Player2 picked '{p2_choice.value}'!")

        if p1_choice == p2_choice:
            return RoundResult.draw

        if (p1_choice == Choice.rock and p2_choice == Choice.scissors or
                p1_choice == Choice.paper and p2_choice == Choice.rock or
                p1_choice == Choice.scissors and p2_choice == Choice.paper):
            return RoundResult.player1_wins

        return RoundResult.player2_wins
