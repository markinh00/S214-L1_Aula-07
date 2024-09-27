import random
from typing import Union

from Choice import Choice
from players.Player import Player


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.choice: Union[Choice, None] = None

    def get_choice(self) -> Choice:
        self.choice = random.choice([Choice.rock, Choice.paper, Choice.scissors])
        return self.choice
