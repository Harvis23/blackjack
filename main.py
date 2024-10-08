import random

suits = ['spades', 'hearts', 'diamons', 'clubs']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal():
    shuffle()
    card = cards.pop()
    return card


card = deal()
print(card)
