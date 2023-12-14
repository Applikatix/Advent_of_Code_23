'''
L = Left, R = Right U = Up, D = Down
'-' = LR
'|' = UD
'J' = LU
'7' = LD
'L' = RU
'F' = RD
'.' = Ø
'S' = Start
'''

def gettile(x: int, y: int):
    return tilemap[y][x]

def walker(prev, curr):
    while True:
        yield curr
        next = nextpoint(prev, curr)
        prev, curr = curr, next

def nextpoint(prev, curr):
    cx, cy = curr
    px, py = prev
    match gettile(cx, cy):
        case '-' if cx - 1 == px:
            return cx+1, cy
        case '-' if cx + 1 == px:
            return cx-1, cy
        case '|' if cy - 1 == py:
            return cx, cy+1
        case '|' if cy + 1 == py:
            return cx, cy-1
        case 'J' if cx - 1 == px:
            return cx, cy-1
        case 'J' if cy - 1 == py:
            return cx-1, cy
        case '7' if cx - 1 == px:
            return cx, cy+1
        case '7' if cy + 1 == py:
            return cx-1, cy
        case 'L' if cx + 1 == px:
            return cx, cy-1
        case 'L' if cy - 1 == py:
            return cx+1, cy
        case 'F' if cx + 1 == px:
            return cx, cy+1
        case 'F' if cy + 1 == py:
            return cx+1, cy

def getstart():
    for y, line in enumerate(tilemap):
        for x, tile in enumerate(line):
            if tile == 'S':
                return x, y

def adjtostart(x, y):
    adj = []

    left = x - 1, y
    right = x + 1, y
    up = x, y - 1
    down = x, y + 1
    if (lt := gettile(*left)) == '-' or lt == 'L' or lt == 'F':
        adj.append(left)
    if (rt := gettile(*right)) == '-' or rt == 'J' or rt == '7':
        adj.append(right)
    if (ut := gettile(*up)) == '|' or ut == '7' or ut == 'F':
        adj.append(up)
    if (dt := gettile(*down)) == '|' or dt == 'J' or dt == 'L':
        adj.append(down)
    
    return adj

def farthestpoint(start):
    p1, p2 = adjtostart(*start)
    for i, (pl, pr) in enumerate(zip(walker(start, p1), walker(start, p2)), 1):
        if pl == pr:
            return i
        if i > 100000000:
            return None

with open('input.txt') as input:
    tilemap = input.read().splitlines()

start = getstart()

print(farthestpoint(start))
