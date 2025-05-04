from character import Charcter
from turn import Turn
from event import Events
from typing import List

class Game:
    def __init__(self):
        self.turn_list: List[Turn] = []
        self.in_game_events: Events = Events()
    
    def act(self) -> None:
        self.now_act: Turn = self.turn_list[0]
        av_cost = self.now_act.get_av()
        for i in range(len(self.turn_list)):
            self.turn_list[i].set_av(self.turn_list[i].get_av() - av_cost)
        self.now_act.act(self)
        self.in_game_events.solve()
        self.change()
    
    def change(self):
        self.turn_list.sort(key=Turn.turn_comparison)