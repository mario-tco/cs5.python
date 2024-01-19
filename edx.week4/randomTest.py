import random

#number = random.randint(1,10)
#print(number)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
random.shuffle(cards)
for index in range(5):
    print(cards[index])