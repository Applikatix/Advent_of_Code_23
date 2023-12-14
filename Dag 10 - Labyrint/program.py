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

def walker(start, curr):
    return (p for p, _ in tilewalker(start, curr))

def tilewalker(start, point):
    px, py = start
    cx, cy = point
    nx, ny = point
    while True:
        match (tile := gettile(cx, cy)):
            case '-' if cx - 1 == px:
                nx = cx+1
            case '-' if cx + 1 == px:
                nx = cx-1
            case '|' if cy - 1 == py:
                ny = cy+1
            case '|' if cy + 1 == py:
                ny = cy-1
            case 'J' if cx - 1 == px:
                ny = cy-1
            case 'J' if cy - 1 == py:
                nx = cx-1
            case '7' if cx - 1 == px:
                ny = cy+1
            case '7' if cy + 1 == py:
                nx = cx-1
            case 'L' if cx + 1 == px:
                ny = cy-1
            case 'L' if cy - 1 == py:
                nx = cx+1
            case 'F' if cx + 1 == px:
                ny = cy+1
            case 'F' if cy + 1 == py:
                nx = cx+1
        yield (cx, cy), tile
        px, py, cx, cy = cx, cy, nx, ny

def getstart():
    for y, line in enumerate(tilemap):
        for x, tile in enumerate(line):
            if tile == 'S':
                return x, y

def adjacent(x, y):
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
    p1, p2 = adjacent(*start)
    for i, (pl, pr) in enumerate(zip(walker(start, p1), walker(start, p2)), 1):
        if pl == pr:
            return i

def looptilemap(start):
    loop = {}
    point, _ = adjacent(*start)
    for p, tile in tilewalker(start, point):
        loop[p] = tile
        if p == start:
            break
    
    res = []
    for y in range(width):
        line = ''
        for x in range(height):
            line += t if (t := loop.get((x, y))) else '.'
        res.append(line)
    return res

with open('input.txt') as input:
    tilemap = input.read().splitlines()
    width = len(tilemap)
    height = len(tilemap[0])

start = getstart()

loopmap = looptilemap(start)

print(*loopmap, sep='\n')
