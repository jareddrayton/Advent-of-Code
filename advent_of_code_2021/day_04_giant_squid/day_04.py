import numpy as np

with open('input.txt', 'r') as f:
    bingo = [line.strip() for line in f.readlines() if line.strip() != '']

numbers = list(map(int, bingo[0].split(',')))
cards = bingo[1:]

new_cards = []

for i in range(0, len(cards), 5):
    new_cards.append(np.array([list(map(int, card.split())) for card in cards[i:i+5]]))

empty_numbers, winning_cards, scores = [], [], []

for number in numbers:
    empty_numbers.append(number)
    for card in new_cards:
        if card.tolist() not in winning_cards:
            masked_array = np.isin(card, empty_numbers)
            is_winning = np.any(np.all(masked_array, axis=0)) or np.any(np.all(masked_array, axis=1))
            if is_winning:
                x = np.ma.array(card, mask=masked_array)
                scores.append(number * np.sum(x))
                winning_cards.append(card.tolist())

print('Part 1:', scores[0])
print('Part 2:', scores[-1])
