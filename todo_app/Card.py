class Card:
    def __init__(self, id, title, status, notes):
        self.id = id
        self.title = title
        self.status = status 
        self.notes = notes

    @classmethod
    def card_content(cls, card, list):
        return cls(card["id"], card["name"], list["name"], card["desc"])
