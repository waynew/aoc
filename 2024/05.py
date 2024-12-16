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
    order_rules = order_rules.split()
    order_rules = [rule.split('|') for rule in order_rules]
    updates = [update.split(',') for update in updates.split('\n')]
    return order_rules, updates


def part_one(data):
    total = 0
    order_rules, updates = split(data)
    priorities = {}
    smallest = 100
    for a,b in order_rules:
        if b not in priorities:
            priorities[b] = min(smallest, 100)
        priorities[a] = priorities[b]-1
        smallest = priorities[a]
    #pprint.pprint(priorities)

    # What does each page belong after?
    afters = collections.defaultdict(set)
    for a,b in order_rules:
        afters[a].add(b)

    #pprint.pprint(afters)
    for update in updates:
        seen = set()
        for page in update:
            seen.add(page)
            after = afters.get(page)
            if after is None:
                continue  # page isn't required before anything
            if any(p in after for p in seen):
                # We already saw this page, but we should not have!
                break
        else:
            # Never broke, never saw invalid page
            mid = len(update)//2
            val = int(update[mid])
            total += val

    return total


class Foo:
    foos = {}
    @classmethod
    def get(cls, val):
        return Foo.foos.setdefault(val, Foo(val))

    def __init__(self, val, next=None):
        self.val = val
        self.before = set()
        if next: 
            self.before.add(Foo.get(next))

    def __str__(self):
        return f"{self.val}\n\t->{self.before}"

    def __repr__(self):
        return str(self)


class Blerp:
    def __init__(self, val, afters=None):
        self.afters = set()
        if afters:
            self.afters.update(afters)
        self.val = val

    def __repr__(self):
        return f"Blerp({self.val!r}, {self.afters!r})"

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return other.val in self.afters

    def __hash__(self):
        return hash(self.val)


def part_two(data):
    total = 0
    order_rules, updates = split(data)

    ranks = {}
    spanks = collections.Counter()
    sorters = collections.defaultdict(set)
    borp = {}
    for rule in order_rules:
        ranks[rule[0]] = 0
        ranks[rule[1]] = ranks.get(rule[1], 0) + 1
        sorters[rule[0]].add(rule[1])
        blerp = borp.setdefault(rule[0], Blerp(rule[0], {rule[1]}))
        borp.setdefault(rule[1], Blerp(rule[1]))
        blerp.afters.add(rule[1])

    vals = sorted(borp, key=lambda x: borp[x])
    #print(vals)

    total_ordered = 0
    for update in updates:
        ordered = sorted(update, key=lambda x: borp[x])
        if update != ordered:
            #print('  ', update, '\n=>', ordered)
            #print('   ', '      '*mid, '^^')
            mid = len(ordered)//2
            val = int(ordered[mid])
            total += val
        else:
            mid = len(ordered)//2
            val = int(update[mid])
            total_ordered += val

    print(total_ordered)
    return total


sample_answer = part_one(puzzle.examples[0].input_data)
print('Sample A', sample_answer)
answer_a = part_one(puzzle.input_data)
print(answer_a)
if not puzzle.answered_a:
    assert sample_answer == 143, str(sample_answer)
    puzzle.answer_a = answer_a

sample_answer = part_two(puzzle.examples[0].input_data)
print('Sample B', sample_answer)
if not puzzle.answered_b:
    answer_b = part_two(puzzle.input_data)
    print(answer_b)
    assert sample_answer == 123, str(sample_answer)
    puzzle.answer_b = answer_b
