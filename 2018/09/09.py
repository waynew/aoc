import io
import re
from ast import literal_eval
from collections import *
from itertools import *

DAY=9

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


def do_it(player_count=30, last_marble=5807):
    scores = Counter()
    for i in range(player_count):
        scores[i+1] = 0
    circle = [0]
    high_marble = current_marble = 0
    current_loc = 0
    current_player = 1
    while current_marble < last_marble:
        high_marble += 1
        if not high_marble % 23:
            scores[current_player] += high_marble
            current_loc -= 7
            if current_loc < 0:
                current_loc = len(circle)+current_loc
            scores[current_player] += circle.pop(current_loc)
            current_marble = circle[current_loc]
        else:
            current_loc += 1
            current_loc = current_loc % len(circle)
            current_loc += 1
            circle.insert(current_loc, high_marble)
            current_marble = high_marble

        #print(current_player, '-', ' '.join(str(x) if x != current_marble else f'({current_marble})' for x in circle))
        current_player = (current_player % player_count) + 1
    return scores



print(f'{" Sample ":*^40}')
result = do_it(30, 5807)
assert result.most_common(1)[0][1] == 37305, result.most_common(1)[0][1]
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY).split()
player_count = int(data[0])
last_marble = int(data[-2])
result = do_it(player_count, last_marble)
print(result.most_common(1))
score = result.most_common(1)[0][1]

result = do_it(player_count, last_marble*100)
print(result.most_common(1))
score = result.most_common(1)[0][1]
#submit1(score)
submit2(result)
print(f'{" Done ":*^40}')
