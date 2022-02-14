from todo_app.Card import Card

class ViewModel: 
    def __init__(self, items: list[Card]):
        self._items: list[Card] = items 
    
    @property
    def items(self) -> list[Card]:
        return self._items

    @property 
    def doing_items(self):
        return [item for item in self._items if item.status == "In Progress"]
    
    @property 
    def not_started_items(self) -> list[Card]:
        return [item for item in self._items if item.status == "Not Started"]

    @property 
    def done_items(self):
        return [item for item in self._items if item.status == "Done"]