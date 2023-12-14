# 0=High card,
# 1=One pair,
# 2=Two pair,
# 3=Three of a kind
# 4=Full house
# 5=Four of a kind
# 6=Five of a kind
def handtype(hand: str):
    cards = {}
    for c in hand:
        cards[c] = cards[c] + 1 if cards.get(c) else 1
    
    jokers = v if (v := cards.pop('J', 0)) else 0
    values = sorted(cards.values(), reverse=True)
    if values:
        values[0] += jokers
    else:
        values = [jokers]
    match values[0]:
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            return 4 if values[1] == 2 else 3
        case 2:
            return 2 if values[1] == 2 else 1
        case _:
            return 0

def cardstrengths(hand: str):
    def f(card: str):
        match card:
            case 'A':
                return 13
            case 'K':
                return 12
            case 'Q':
                return 11
            case 'T':
                return 10
            case 'J':
                return 1
            case c:
                return int(c)
    return [f(card) for card in hand]

with open('input.txt') as input:
    hands = [(hand, int(bid)) for hand, bid in (line.split() for line in input)]
    hands.sort(key=lambda h: (handtype(h[0]), *cardstrengths(h[0])))
    res = sum((i+1) * bid for i, (_, bid) in enumerate(hands))
    print('sum af point:', res)
