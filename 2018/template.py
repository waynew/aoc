import io
import re
from ast import literal_eval
from collections import *
from itertools import *

sample_1 = io.StringIO('''
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
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
    print(lines)
    print('==== End part one ====')


print(f'{" Sample ":*^40}')
part_one(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
#part_one(lines)
print(f'{" Done ":*^40}')
