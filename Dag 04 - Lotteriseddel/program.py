pointtotal = 0
cardtotal = 0
cards = {i:1 for i in range(188)}

with open('input.txt') as input:
    for i, card in enumerate(input):
        _, numbers = card.split(':', 1)
        wins, nums = numbers.split('|', 1)

        points = 0
        score = 0
        for n in nums.split():
            if n in wins.split():
                points = points*2 if points else 1
                score += 1
        
        for j in range(i+1, i+score+1):
            cards[j] += cards[i]
        
        pointtotal += points
        cardtotal += cards[i]

print(f'points: {pointtotal}')
print(f'cards: {cardtotal}')
