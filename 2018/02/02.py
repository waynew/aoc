from collections import Counter


def checksum(word):
    c = Counter()
    for letter in word:
        c[letter] += 1
    return c

def has_2(counts):
    for a in counts:
        if counts[a] == 2:
            return True
    return False

def has_3(counts):
    for a in counts:
        if counts[a] == 3:
            return True
    return False


print('=== Sample ===')
twos = 0
threes = 0
for line in [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
]:
    check = checksum(line)
    twos += has_2(check)
    threes += has_3(check)
print(twos, threes, twos*threes)
print('=== End Sample ===')
print()
print()

print('Part 1:')
with open('input.txt') as f:
    twos = 0
    threes = 0
    for line in f:
        counts = checksum(line.strip())
        twos += has_2(counts)
        threes += has_3(counts)

print(twos, threes, twos*threes)

def compare(one, two):
    count = 0
    for a,b in zip(one, two):
        if a != b:
            count += 1
    if count == 1:
        return True
    return False

print('Part 2:')
with open('input.txt') as f:
    ids = list(line.strip() for line in f)
    for i in range(len(ids)):
        for other in ids[i:]:
            if compare(ids[i], other):
                print(ids[i], other, sep='\n')
                for a, b in zip(ids[i], other):
                    if a == b:
                        print(a, end='')
                print()
