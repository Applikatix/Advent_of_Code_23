import re

sum = 0
gearsum = 0

with open('input.txt', 'r') as input:
    # map[row][col]
    map = [line[:-1] for line in input]
    width = len(map[0])
    lastcol = width - 1
    lastrow = len(map) - 1

    numbers = [[match for match in re.finditer(r'\d+', line)] for line in map]
    for row, ns in enumerate(numbers):
        for num in ns:
            n = int(num[0])
            start, end = num.span()

            searchspace = ''

            if start > 0:
                start -= 1
                searchspace += map[row][start]
            if end < width:
                searchspace += map[row][end]
                end += 1
            
            if row > 0:
                searchspace += map[row - 1][start:end]
            if row < lastrow:
                searchspace += map[row + 1][start:end]
            
            if re.search(r'[^0-9\.]', searchspace):
                sum += n
    
    gears = [[match for match in re.finditer(r'\*', line)] for line in map]
    for row, gs in enumerate(gears):
        for gear in gs:
            col = gear.start()
            points = [
                (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
            
            nums = {
                (y, num.start()):int(num[0])
                for y, x in points
                for num in numbers[y]
                if x in range(num.start(), num.end())
            }

            if len(nums) == 2:
                a, b = [n for n in nums.values()]
                gearsum += a * b

print(sum)
print(gearsum)
