from re import findall

regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

def get_num(str):
    if str == 'one':
        return '1'
    elif str == 'two':
        return '2'
    elif str == 'three':
        return '3'
    elif str == 'four':
        return '4'
    elif str == 'five':
        return '5'
    elif str == 'six':
        return '6'
    elif str == 'seven':
        return '7'
    elif str == 'eight':
        return '8'
    elif str == 'nine':
        return '9'
    else:
        return str

sum = 0

with open('input.txt', 'r') as input:
    for line in input:
        digits = findall(regex, line)

        sum += int(get_num(digits[0]) + get_num(digits[-1]))

print(sum)
