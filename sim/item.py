import string

class Item():
    def __init__(self, name, ticker, category, weight, volume) -> None:
        self.name: string = name
        self.ticker: string = ticker
        self.category: string = category
        self.weight: float = weight
        self.volume: float = volume