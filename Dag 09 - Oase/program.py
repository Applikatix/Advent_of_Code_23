def differences(his: list[int]):
    return [his[i+1] - his[i] for i in range(len(his) - 1)]

def getdiff(his: list[int]):
    difflevels = [his]
    while True:
        nextlvl = differences(difflevels[-1])
        difflevels.append(nextlvl)
        if not any(nextlvl):
            return difflevels

def predictnext(difflevels: list[list[int]]):
    res = 0
    for *_, last in reversed(difflevels):
        res += last
    return res

def predictprev(difflevels: list[list[int]]):
    res = 0
    for first, *_ in reversed(difflevels):
        res = first - res
    return res

with open('input.txt') as input:
    histories = [[int(n) for n in his.split()] for his in input]

res = sum(predictnext(getdiff(his)) for his in histories)
print(res)
res = sum(predictprev(getdiff(his)) for his in histories)
print(res)
