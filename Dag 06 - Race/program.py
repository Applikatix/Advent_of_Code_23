def winconditions(time: int, recorddist: int):
    return sum(
        1 for holdtime in range(time)
        if holdtime * (time - holdtime) > recorddist)

with open('input.txt') as input:
    _, *times = next(input).split()
    _, *distances = next(input).split()
    
    races = [(int(t), int(d)) for t, d in zip(times, distances)]
    res = 1
    for win in (winconditions(*race) for race in races):
        res *= win
    print('wins1:', res)
    
    longrace = (int(''.join(times)), int(''.join(distances)))
    res = winconditions(*longrace)
    print('wins2:', res)
