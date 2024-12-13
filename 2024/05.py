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



def part_one(data):
    befores = collections.defaultdict(set)
    order_rules, updates = data.split('\n\n')
    order_rules = sorted(order_rules.split(), key=lambda x: x.split('|')[1])
    updates = updates.split('\n')


    ordered = list(order_rules.pop().split('|'))
    while order_rules:
        before, after = order_rules.pop().split('|')


    print(order_rules[:10])
    for update in updates:
        pass
    return 0
    print(updates[:10])
    #print(befores)
    #print(data)
    #submit(..., part="a", day=DAY, year=2024, reopen=False)

def part_two(data):
    ...
    #submit(..., part="b", day=DAY, year=2024, reopen=False)


sample_answer = part_one(puzzle.examples[0].input_data)
assert sample_answer == 143, str(sample_answer)
if not puzzle.answered_a:
    answer_a = part_one(puzzle.input_data)

sample_answer = part_two(puzzle.examples[0].input_data)
assert sample_answer == 'asdf', str(sample_answer)
if not puzzle.answered_b:
    answer_b = part_two(puzzle.input_data)
