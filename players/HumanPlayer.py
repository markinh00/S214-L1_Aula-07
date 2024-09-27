from typing import Union
from Choice import Choice
from players.Player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.choice: Union[Choice, None] = None

    def get_choice(self) -> Choice:
        possible_choices = ["rock", "paper", "scissors"]

        while True:
            human_input = input("Please type in your choice between rock, paper, scissors: ")
            if human_input not in possible_choices:
                print(f"'{human_input}' is not a valid choice!")
            else:
                break

        if human_input == Choice.rock.value:
            self.choice = Choice.rock
        elif human_input == Choice.paper.value:
            self.choice = Choice.paper
        elif human_input == Choice.scissors.value:
            self.choice = Choice.scissors

        return self.choice
