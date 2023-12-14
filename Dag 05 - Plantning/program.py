class MapRange:
    def __init__(self, deststart, sourcestart, rangelen):
        self.start = int(sourcestart)
        self.end = self.start + int(rangelen)
        self.conv = int(deststart) - self.start
    
    def convertint(self, n: int):
        return n + self.conv if self.start <= n and n < self.end else None

with open('input.txt') as input:
    seeds = [int(seed) for seed in next(input).split(':', 1)[1].split()]
    
    maps: dict[str, list[MapRange]] = {}
    mapkey = ''
    for line in input:
        elems = line.split()
        if not elems:
            continue
        elif elems[1] == 'map:':
            mapkey = elems[0]
            maps[mapkey] = []
        else:
            maps[mapkey].append(MapRange(*elems))
    
    #v1
    minloc = 1000000000
    for seed in seeds:
        for mapranges in maps.values():
            for mapran in mapranges:
                if (n := mapran.convertint(seed)) != None:
                    seed = n
                    break
        if seed < minloc:
            minloc = seed
    print(f'min location 1: {minloc}')
    
    #v2
    iter = iter(seeds)
    seeds = sorted(
        ((seed, seed + next(iter)) for seed in iter),
        key=lambda x: x[0])
    
    for mapping in maps.values():
        mapping.sort(key=lambda m: m.start)
        res: list[tuple[int, int]] = []
        for seedstart, seedend in seeds:
            for maprange in mapping:
                if not seedstart < seedend:
                    break
                if not seedstart < maprange.end:
                    pass
                elif maprange.start < seedend:
                    def convert(start: int, end: int):
                        return (start + maprange.conv, end + maprange.conv)

                    if maprange.start <= seedstart:
                        end = min(maprange.end, seedend)
                        res.append(convert(seedstart, end))
                        seedstart = end
                    else:
                        res.append((seedstart, maprange.start))
                        seedstart = maprange.start
                else:
                    res.append((seedstart, seedend))
                    break
        seeds = sorted(res, key=lambda s: s[0])
    print('min location 2:', min(seed[0] for seed in seeds))
