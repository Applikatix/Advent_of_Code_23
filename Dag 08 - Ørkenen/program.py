from re import findall
from itertools import cycle
from math import lcm

with open('input.txt') as input:
    instruction = cycle(next(input)[:-1])
    next(input)
    nodes = {k:(l,r) for k, l, r in (findall(r'[A-Z]{3}', line) for line in input)}

# Del 1

current = 'AAA'
steps = 0
while current != 'ZZZ':
    left, right = nodes[current]
    current = left if next(instruction) == 'L' else right
    steps += 1

print('result 1:', steps)

# Del 2

paths = [k for k in nodes if k[2] == 'A']

counts = []
for current in paths:
    i = 0
    while current[2] != 'Z':
        left, right = nodes[current]
        current = left if next(instruction) == 'L' else right
        i += 1
    counts.append(i)

steps = lcm(*counts)
print('result 2:', steps)
