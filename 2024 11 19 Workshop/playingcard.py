class PlayingCard:
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    suits = {'d': "Diamonds", 'c': "Clubs", 'h': "Hearts", 's': "Spades"}
    def __init__(self, rank: int, suit: str):
        if (not (0 < rank < 14)):
            raise ValueError("rank must be an integer with a value between 0 and 14")
        if not ((suit == 'd') or (suit == 'c') or (suit == 'h') or (suit == 's')):
            raise ValueError("suit must be a string with value of 'd', 'c', 'h', or 's'")
        self.rank = rank
        self.suit = self.suits[suit]
        
    def get_rank(self) -> int:
        return self.rank
        
    def get_suit(self) -> int:
        return self.suit
            
    def value(self) -> int:
        if (self.rank >= 10):
            return 10
        return self.rank

    def __str__(self) -> str:
        card = self.cards[self.rank-1]
        return f"{card} of {self.suit}"
    
c = PlayingCard(13, "s")
print(f"{c.get_rank()}")
print(f"{c.get_suit()}")
print(f"{c.value()}")
print(f"{c.__str__()}")
