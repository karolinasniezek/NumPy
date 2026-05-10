import numpy as np

def move_character_on_board(position, move, board):

    x,y = position
    dx, dy = move

    # 1. Set player on initial position
    board[x, y] = 1

    # 2. Position vector and translation matrix
    position_vector = np.array([x,y,1])

    # 3. Translation matrix
    translation_matrix = np.array(([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ]))

    # 4. New position of player
    new_position = np.matmul(translation_matrix, position_vector.T)
    new_x, new_y = new_position[0], new_position[1]

    # note!: make sure that player is staying on the board
    new_x = int(min(max(new_x, 0), board.shape[0] -1))
    new_y = int(min(max(new_y, 0), board.shape[1] -1))

    # 5. Update board
    board[x,y] = 0
    board[new_x, new_y] = 1

    return new_x, new_y, board

board = np.zeros((5, 5), dtype=int)

position = (2, 2)
move = (1, -1)

new_x, new_y, updated_board = move_character_on_board(
    position,
    move,
    board
)

print("New position:", (new_x, new_y))
print(updated_board)
