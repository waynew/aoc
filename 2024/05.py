import pprint
from functools import cmp_to_key
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

    r
    befores = collections.defaultdict(set)
    order_rules, updates = split(data)
    uniques = set()
    for rule in order_rules:
        uniques.update(rule)
        befores[rule[0]].add(rule[1])
    #pprint.pprint(uniques)
    asdf = sorted(uniques, key=cmp_to_key(lambda x,y: -1 if x in befores and y in befores[x] else 0))
    #print(asdf)

    total = 0
    good_updates = []
    for update in updates:
        last_i = -1
        for num in update:
            if num in asdf:
                idx = asdf.index(num)
            else:
                idx = last_i
            if idx <= last_i:
                break
            last_i = idx
        else:
            good_updates.append(update)
            total += int(update[len(update)//2])
    #pprint.pprint(good_updates)
    print(total)


    return total

def part_two(data):
    ...
    #submit(..., part="b", day=DAY, year=2024, reopen=False)


sample_answer = part_one(puzzle.examples[0].input_data)
if not puzzle.answered_a:
    answer_a = part_one(puzzle.input_data)
    print(answer_a)
    assert sample_answer == 143, str(sample_answer)
    #puzzle.answer_a = answer_a

sample_answer = part_two(puzzle.examples[0].input_data)
assert sample_answer == 'asdf', str(sample_answer)
if not puzzle.answered_b:
    answer_b = part_two(puzzle.input_data)
