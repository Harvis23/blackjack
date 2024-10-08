import random

suits = ['spades', 'hearts', 'diamons', 'clubs']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

random.shuffle(cards)
# pop a card from the cards list
card = cards.pop()
print(card)