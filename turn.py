from character import Charcter
from eventable import Eventable
from game import Game
from typing import Any

class Turn:
    def __init__(self, main_unit: Charcter | Eventable) -> None:
        self.main_unit: Charcter | Eventable = main_unit
        self.typical: bool = True
        self.av: float = 0
    
    def get_main_unit(self) -> Charcter | Eventable:
        return self.main_unit
    
    def act(self, game_stamp: Game) -> None:
        self.main_unit.act(game_stamp)
    
    def get_av(self) -> float:
        return self.av
    
    def set_av(self, new_av: float | int | Any) -> None:
        self.av = float(new_av)
    
    @staticmethod
    def turn_comparison(turn) -> float:
        return turn.av