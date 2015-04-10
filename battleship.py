__author__ = 'donnywdavis'
__project__ = 'Battleship'

# Create our 10x10 grid for the game board
grid = []
for index in range(10):
    grid.append(["O"] * 10)


# Draw the board to the screen
def draw_board(board):
    for row in board:
        print(" ".join(row))


draw_board(grid)