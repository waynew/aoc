import io

sample = io.StringIO("""\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""")

def to_stacks(f, count):
    stacks = {i: [] for i in range(1, count+1)}
    for line in f:
        if not line.strip():
            return stacks
        if ''.join(line.split()) == ''.join(str(x) for x in range(1, 1+count)):
            pass
        else:
            line = f"{line}{' '*count*4}"
            indexes = list(range(1, count*4-1, 4))
            #print(indexes)
            #print(line)
            crates = [line[x] for x in indexes]
            #print(crates)
            for i in range(count):
                crate = crates[i]
                if crate.strip():
                    stacks[i+1].insert(0, crate)
    assert False, "Crate input never ended!"


def get_count(file):
    prev_line = None
    for line in file:
        if not line.strip():
            count = len(prev_line.strip().split())
            return count
        prev_line = line
    assert False, "Unable to find count line"


def move_stacks(stacks, file):
    for line in file:
        move = line.split()
        count, src, dst = int(move[1]), int(move[3]), int(move[5])
        for i in range(count):
            stacks[dst].append(stacks[src].pop())
    return stacks


def move_stacks_two(stacks, file):
    for line in file:
        move = line.split()
        count, src, dst = int(move[1]), int(move[3]), int(move[5])
        leave, move = stacks[src][:-count], stacks[src][-count:]
        stacks[dst].extend(move)
        stacks[src] = leave
    return stacks


def top_crates(stacks):
    for i in range(len(stacks)):
        print(stacks[i+1][-1], end='')
    print()

def part_one(file):
    count = get_count(file)
    file.seek(0)
    stacks = to_stacks(file, count)
    #print(stacks)
    #exit()
    stacks = move_stacks(stacks, file)
    top_crates(stacks)


def part_two(file):
    count = get_count(file)
    file.seek(0)
    stacks = to_stacks(file, count)
    #print(stacks)
    #exit()
    stacks = move_stacks_two(stacks, file)
    top_crates(stacks)


part_one(sample); sample.seek(0)
part_two(sample); sample.seek(0)
with open('input.txt') as f:
    part_one(f); f.seek(0)
    part_two(f); f.seek(0)
