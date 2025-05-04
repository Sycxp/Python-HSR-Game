from typing import List

class Event:
    def __init__(self):
        pass
    
    def solve(self, event_list: List):
        pass

class Events:
    def __init__(self) -> None:
        self.event_list: List[Event] = []
    
    def solve(self) -> None:
        new_event_list = []
        for i in self.event_list:
            new_event_list = i.solve(new_event_list)
        self.event_list = new_event_list