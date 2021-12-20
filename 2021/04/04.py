import itertools
import io
from pprint import pprint

sample_data = io.StringIO('''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''.strip())


def boards_and_numbers(data):
    numbers = [int(num) for num in data.readline().split(',')]
    data.readline()
    boards = []
    for boardlines in data.read().split('\n\n'):
        board = {'B':[], 'I': [], 'N': [], 'G': [], 'O': []}
        for line in boardlines.split('\n'):
            for letter, number in zip('BINGO', line.strip().split()):
                board[letter].append(int(number))
        boards.append(board)

    return numbers, boards


def has_won(board):
    '''
    Take a BINGO board and return True if the board has any winning rows
    or columns. Diagonals or blackouts are not considered.
    '''

    # column check
    # B  I  N  G  O
    # 22  x 17 11  0
    #  8  x 23  4 24
    # 21  x 14 16  7
    #  6  x  3 18  5
    #  1  x 20 15 19
    for letter in 'BINGO':
        if all(num == 'x' for num in board[letter]):
            return True

    # row check
    #
    # B  I  N  G  O
    # 22 13 17 11  0
    #  x  x  x  x  x
    # 21  9 14 16  7
    #  6 10  3 18  5
    #  1 12 20 15 19
    for i in range(5):
        for letter in 'BINGO':
            if board[letter][i] != 'x':
                break
        else:
            return True
    return False


def when_wins(numbers, board):
    '''
    Given the list of bingo numbers called, return the turn number, score and
    winning board.

    Winning board will have called numbers replaced by the letter x.
    
    22 13 17 11  0
     8  2 23  4 24
    21  9 14 16  7
     6 10  3 18  5
     1 12 20 15 19
    '''
    board = board.copy()
    unmarked_numbers = set(itertools.chain(*board.values()))
    for turns, number in enumerate(numbers, start=1):
        for letter in 'BINGO':
            try:
                i = board[letter].index(number)
            except ValueError:
                pass
            else:
                board[letter][i] = 'x'
                unmarked_numbers.remove(number)

        if has_won(board):
            #print(unmarked_numbers)
            score = sum(unmarked_numbers) * number
            return turns, score, board
        #print_bingo(board)
        #print('*'*40)
        #print(len(unmarked_numbers))
    #import pprint; pprint.pprint(board)


def print_bingo(board):
    template = '{:>2} {:>2} {:>2} {:>2} {:>2}'

    print(template.format(*'BINGO'))
    for i in range(5):
        print(template.format(*(board[letter][i] for letter in 'BINGO')))


def one(file):
    numbers, boards = boards_and_numbers(file)
    #print(numbers, boards)

    ranks = []
    for board in boards:
        ranks.append(when_wins(numbers=numbers, board=board))

    ranks.sort()
    print(ranks[0][0], ranks[0][1])
    print_bingo(ranks[0][2])

    # lol - this is part 2
    print(ranks[-1][0], ranks[-1][1])
    print_bingo(ranks[-1][2])


    #print(winning_turn)
    #pprint(board)

    ...


def two(data):
    ...


if __name__ == '__main__':
    #print(one(sample_data)); exit()
    with open('input.txt') as f:
        one(f)
