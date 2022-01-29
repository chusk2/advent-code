# use numpy to deal with large amount of numbers
import numpy as np

# retrive data from text files
with open('input_day4 - drawn number sample.txt', 'r') as file:
    drawn_numbers = []
    for line in file.readlines():
        drawn_numbers += line.strip().split(',')
drawn_numbers = [int(i) for i in drawn_numbers]

with open('input_day4 - bingo boards sample.txt', 'r') as file:
    # in the text file, set last line to EOF
    bingo_boards = []
    board = []
    for line in file.readlines():
        # new blank line means there is a new board.
        # In this case store the previous board
        if line not in ['\n', 'EOF']:
            row = line.strip().split()
            row = [int(i) for i in row]
            board.append(row)
        else:
            board = np.array(board)
            bingo_boards.append(board)
            board = []

# Create lists filled with a boolean array (True if number has been drawn)
# and a wins counter for each bingo board
bool_boards = [
    [np.full(25, False).reshape(5, 5), 0] for i in range(len(bingo_boards))
]


def check_line(bool_board):
    """
    Checks if all elements of a row or a column are True.
    In that case, the board has completed a line
    """

    # check line in rows
    for i in range(5):
        # check if all the elements of the row are True
        if bool_board[i, :].all():
            return True

    # check if all the elements of the column are True
    for j in range(5):
        if bool_board[:, j].all():
            return True


check_numbers = True

# check every drawn number against bingo boards
index_number = 0
index_board = 0

while check_numbers:

    while True:
        number = drawn_numbers[index_number]
        board = bingo_boards[index_board]
        boolean = bool_boards[index_board][0]
        win_counter = bool_boards[index_board][1]

        # check if the drawn number is in the board
        if number in board:
            # return the position of the drawn number in the bingo board
            positions = np.where(board == number)
            row = positions[0]
            col = positions[1]
            # replace with True at position of number match
            # in the bingo board
            boolean[row, col] = True
            # +1 to board wins counter
            win_counter += 1

        # check for line because board has at least 5 wins
        if win_counter >= 5:
            if check_line(boolean):
                total = np.sum(board[boolean])
                print(f'Board {index_board} has a line')
                print(f'The sum is {total}')
                check_numbers = False
                break
        # check next board
        if index_board < len(bingo_boards) - 1:
            index_board += 1
        else:
            break

    # reset the index for boards to zero before checking all bool_boards
    # with the new number
    index_board = 0
    # all boards were checked against drawn numbers
    # try with next number
    if index_number < len(drawn_numbers) - 1:
        index_number += 1
    else:
        break
print(drawn_numbers)