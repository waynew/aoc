import io

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

with open('input.txt') as real_input:
    lines = [line.strip() for line in real_input]

sample_1_lines = [line.strip() for line in sample_1]
sample_2_lines = [line.strip() for line in sample_2]


def part_one(lines):
    print('==== Part one ====')
    print(lines)
    print('==== End part one ====')


def part_two(lines):
    print('==== Part two ====')
    print(lines)
    print('==== End part two ====')


print('***** Sample ******')
part_one(sample_1_lines)
part_two(sample_2_lines)
print('***** End Sample ******')

print()
print()

#part_one(lines)
#part_two(lines)
