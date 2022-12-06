# Okay, here we go! Lanternfish time...

# Here's our sample initial state:

initial_state = [3,4,3,1,2]


def do_a_day(state):
    new_fishies = 0
    for i in range(len(state)):
        if state[i] == 0:
            new_fishies += 1
            state[i] = 7
    for i in range(len(state)):
        state[i] -= 1
    if new_fishies:
        for i in range(new_fishies):
            state.append(8)
    return state


if __name__ == "__main__":
    #print(do_a_day(initial_state)); exit()   # okay, looks like the sample output
    #Initial state: 3,4,3,1,2
    #After  1 day:  2,3,2,0,1
    #                     *
    #After  2 days: 1,2,1,6,0,8
    #                         *
    #After  3 days: 0,1,0,5,6,7,8
    #[3, 4, 3, 1, 2]
    #[2, 3, 2, 0, 1]
    #[1, 2, 1, 6, 0, 8]
    #[0, 1, 0, 5, 6, 7, 8]
    # okay, looking good, let's try 18 days
    #After  4 days: 6,0,6,4,5,6,7,8,8
    #After  5 days: 5,6,5,3,4,5,6,7,7,8
    #After  6 days: 4,5,4,2,3,4,5,6,6,7
    #After  7 days: 3,4,3,1,2,3,4,5,5,6
    #After  8 days: 2,3,2,0,1,2,3,4,4,5
    #After  9 days: 1,2,1,6,0,1,2,3,3,4,8
    #After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
    #After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
    #After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
    #After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
    #After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
    #After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
    #After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
    #After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
    #After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
    #              [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
    # very good!
    # okay, so 80 days with my actual input...

    state = initial_state
    initial_fishies = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
    }
    for i in state:
        initial_fishies[i] += 1
    day = min(state)
    print(initial_fishies)

    # if you can't tell yet - basically I want to say, today is day X, and then
    # the day just ticks along, and every fish who makes babies on that day adds fish
    # to the appropriate pool. Lemme double check this for a second...

    # okay, so on the day of birth, the child fish will have +2 babyday

    # bah... i think that's gonna be the wrong way. Let me try to just try one
    # fishy

    #print('*'*20)
    #fish = [1]
    #initial_fishies = {0:0, 1:1, 2:0, 3:0, 4:0, 5:0, 6:0}
    #for i in range(10):
    #    do_a_day(fish)
    #    #print(i)
    #fishies = initial_fishies.copy()
    #day = 2
    #for i in range(10):
    #    day -= 1
    #    day = day % 7
    #    birthday_fishies = (day + 2) % 7
    #    fishies[birthday_fishies] += fishies[day]
    #    print(day, birthday_fishies)

    # this does not appear to be working the way I was hoping.

    # Well, 256 took way too long for that number...
    #print(fishies)
    #print(fish)
    #print(len(fish))
    #exit()

    # Okay, so... 1,2,3,4,5,6
    #
    # That means...
    # hrm.
    # It's pretty late here, so I may call it a day for now...

    #for i in range(256):
    #    state = do_a_day(state)
    #    print(i)
    #print(len(state))
    # okay, so... what's our formula?
    #Initial state: 3,4,3,1,2
    # days / 7 gives the number of cycles, right? So... 18/7 = 2 cycles (and some)
    # Oooo, okay, let's try that? I think there's some type of modulo for the current fish age... though part of me wonders if I'm over thinking it...
    # I might be. Let's try a slightly different tack...


    exit()

    with open('input.txt') as f:
        data = [int(x) for x in f.readline().strip().split(',')]

    for i in range(80):
        data = do_a_day(data)

    # Woohoo! Worked
    print("Part 1:", len(data))

    # O nice
