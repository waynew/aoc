import io

sample = io.StringIO('''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''.strip())


def part_one(f):
    most_cals = 0
    elf = 1
    max_elf = None
    total = 0
    elves = [
        [int(l) for l in lines.split()] for lines in
        f.read().split('\n\n') 
    ]
    print(len(elves))
    sums = [sum(c) for c in elves]
    print('This one:', sorted(sums)[-3:], sum(sorted(sums)[-3:]))
    print(sorted(elves, key=lambda x: sum(x))[:5])
    return max(sums), sums[-3:], sum(sums[-3:])

    for line in f:
        line = line.strip()
        if not line:
            elves.append(total)
            if total > most_cals:
                most_cals = total
                max_elf = elf
            total = 0
            elf += 1
        else:
            total += int(line)
    elves.append(total)
    top_3 = sorted(elves)[-3:]
    return max_elf, most_cals, top_3, sum(top_3)

print(part_one(sample))
with open('input.txt', 'r') as f:
    print(part_one(f))


