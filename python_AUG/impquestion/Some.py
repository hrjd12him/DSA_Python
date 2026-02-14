# Sudko Code Validation

# We have the Input of 9*9 array that means 2 D array  we need to

# task to be Done
"""1. i need to check rows
2. i need to check colums
3. check 3*3 nlocks

"""


# output belongs to be Bool
def validate_sudoku(board):

    req = set(range(1, 10))
    # [1,2,3,4,5,6,7,8,9]
    for row in board:
        if set(row) != req:
            return False

    for col in zip(*board):
        if set(col) != req:
            return False

    # check for 3*3 Kind Of sliding window Concept Doing This Using Indexing
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            block = []

            for i in range(3):
                for j in range(3):
                    block.append(board[box_row + i][box_col + j])

            if set(block) != req:
                return False

    return True


# Time Complaxity is O(9*9)
# O(81)

# space Complaxity  = O(1)
base = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]

result = validate_sudoku(base)
print(result)
