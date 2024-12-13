import pprint
from aocd import get_data, submit
import aocd
import collections

DAY=5

puzzle = aocd.get_puzzle(year=2024, day=DAY)
data = puzzle.input_data
data=sample_data = '''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''.strip()



def the_order(data, k, seen):
    print(k)
    if k in seen:
        return False
    seen.add(k)
    next = data.get(k)
    if next:
        the_order(data, next, seen)
    return True


def split(data):
    order_rules, updates = data.split('\n\n')
    order_rules = sorted(order_rules.split())
    order_rules = [rule.split('|') for rule in order_rules]
    updates = [update.split(',') for update in updates.split('\n')]
    return order_rules, updates


def part_one(data):
    befores = collections.defaultdict(set)
    order_rules, updates = split(data)
    uniques = set()
    ordered = []
    something = {}
    for before, after in order_rules:
        if after in order_rules:
            ordered.insert(order_rules.index(after), before)

        if after in something:
            pass
        else:
            something[before] = after

        uniques.add(before)
        uniques.add(after)
        #print(before, after)
        befores[after].add(before)

    
    print(uniques)
    print(something)
    pprint.pprint(befores)
    #print(len(updates),sum(len(u) for u in updates))
    #print('*'*20)
    print(min(len(befores[b]) for b in befores))
    #print(len(befores))
    #print(len(order_rules))
    #print(order_rules)
    #print(updates[0])
    return
    for update in updates:
        for page in update:
            print(the_order(order_rules, page, set()))

        print()
        print('*'*20)
        break

    return 0
    print(updates[:10])
    #print(befores)
    #print(data)
    #submit(..., part="a", day=DAY, year=2024, reopen=False)

def part_two(data):
    ...
    #submit(..., part="b", day=DAY, year=2024, reopen=False)


sample_answer = part_one(puzzle.examples[0].input_data)
if not puzzle.answered_a:
    answer_a = part_one(puzzle.input_data)
exit()
assert sample_answer == 143, str(sample_answer)

sample_answer = part_two(puzzle.examples[0].input_data)
assert sample_answer == 'asdf', str(sample_answer)
if not puzzle.answered_b:
    answer_b = part_two(puzzle.input_data)
