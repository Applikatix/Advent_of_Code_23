
sum = 0
pow_sum = 0

with open('input.txt') as input:
    for line in input:
        split = line.split(':')
        
        id = int(split[0][5:])
        cubes = [cube for draw in split[1].split(';') for cube in draw.split(',')]
        
        max_r = 0
        max_g = 0
        max_b = 0

        for cube in cubes:
            n, color = cube.split()
            n = int(n)

            match color:
                case 'red' if n > max_r:
                    max_r = n
                case 'green' if n > max_g:
                    max_g = n
                case 'blue' if n > max_b:
                    max_b = n

        if max_r <= 12 and max_g <= 13 and max_b <= 14:
            sum += id
        
        pow_sum += max_r * max_g * max_b

print(sum)
print(pow_sum)
