import io
import re
import logging
from ast import literal_eval
from collections import *
from itertools import *

logging.basicConfig(
    filename='debug.txt',
    filemode='w',
    level=logging.INFO,
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
        can_synth = a.lower() == b.lower()
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
            i -= 1
            i = max(0, i)
            debug(text[start:end])
        else:
            i += 1
    print(len(text))
    print('==== End part one ====')


print(f'{" Sample ":*^40}')
part_one(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
part_one(lines)
print(f'{" Done ":*^40}')
