import io
import re
from ast import literal_eval
from collections import *
from itertools import *

DAY=0

try:
    from aocd import get_data, submit1, submit2
except:
    def get_data(day=None):
        try:
            with open('input.txt') as real_input:
                return real_input.read()
        except FileNotFoundError:
            print('WARNING: no input.txt found, just running with sample data')

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

sample_1_lines = [line.strip() for line in sample_1]
sample_2_lines = [line.strip() for line in sample_2]


def do_it(lines):
    print(lines)


print(f'{" Sample ":*^40}')
result = do_it(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY)
#result = do_it(lines)
#part_one(lines)
#submit1(result)
#submit2(result)
print(f'{" Done ":*^40}')
