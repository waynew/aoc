import io
import re
import logging
from ast import literal_eval
from collections import *
from itertools import *

logging.basicConfig(
    filename='debug.txt',
    filemode='w',
    level=logging.WARN,
)

logger = logging.getLogger('day05')
debug = logger.debug

sample_1 = io.StringIO('''
dabAcCaCBAcCcaDA
'''.strip())

sample_2 = io.StringIO('''
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
'''.strip())

try:
    with open('input.txt') as real_input:
        lines = [line.strip() for line in real_input]
except FileNotFoundError:
    print('WARNING: no input.txt found, just running samples')

sample_1_lines = [line.strip() for line in sample_1]
sample_2_lines = [line.strip() for line in sample_2]


def part_one(lines):
    print('==== Part one ====')
    text = lines[0]
    i = 0
    while i < len(text)-1:
        a,b = text[i:i+2]
        can_synth = a.lower() == b.lower() and a != b
        if can_synth:
            logger.info(a+b)
            debug(f'synthing {a} {b}')
            start = max(0, i-10)
            end = start+10
            disp = text[start:end]
            spaces = disp.find(a+b)
            debug(' '*spaces+'vv')
            debug(text[start:end])
            debug(' '*spaces+'^^')
            text = text[:i] + text[i+2:]
            debug(text[start:end])
            i -= 1
            i = max(0, i)
        else:
            i += 1
    print(len(text))
    print('==== End part one ====')
    return len(text)


def part_two(lines):
    original_text = text = lines[0]
    units = set(text)
    pairs = defaultdict(list)
    for unit in units:
        pairs[unit.lower()].append(unit)
    lengths = []
    for unit in pairs:
        text = original_text
        for thing in pairs[unit]:
            text = text.replace(thing, '')
        lengths.append(part_one([text]))
    print('Min:', min(lengths))


print(f'{" Sample ":*^40}')
part_one(sample_1_lines)
part_two(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
part_one(lines)
part_two(lines)
print(f'{" Done ":*^40}')
