from aocd import get_data, submit
from collections import Counter
import re

DAY=3

data = sample_data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
data = get_data(year=2024, day=DAY)
MUL_PATTERN = r'mul\((\d+),(\d+)\)'


def part_one(data):
    uncorrupted = re.findall(MUL_PATTERN, data)
    total = 0
    for mul in uncorrupted:
        a, b = mul
        total += int(a) * int(b)
    print(total)
    #submit(total, part="a", day=DAY, year=2024, reopen=False)

def part_two(data):
    enabled = True
    i = 0
    total = 0
    while i < len(data):
        char = data[i]
        #print(data[i:i+7])
        if char == 'd':
            if data[i:].startswith('do()'):
                #print('do')
                i += 4
                enabled = True
            elif data[i:].startswith("don't()"):
                #print('dont')
                i += 7
                enabled = False
            else:
                i += 1
        elif char == 'm':
            match = re.match(MUL_PATTERN, data[i:])
            if match:
                a, b = (int(i) for i in match.groups())
                i += match.end()
                if enabled:
                    total += a*b
            else:
                i += 1
        else:
            i += 1
    print(total)
    #submit(total, part="b", day=DAY, year=2024, reopen=False)


part_one(data)
part_two(data)
