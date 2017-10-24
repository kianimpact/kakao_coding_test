m = int(input())
n = int(input())
board = [[0] * n for i in range(m)]

for row, row_val in enumerate(input().replace('“', '').replace('”', '').replace('[', '').replace(']', '').split(', ')):
    for col, col_val in enumerate(row_val):
        board[row][col] = col_val


def make_board_destroyed(board, destroyed_block_result):
    for row, row_val in enumerate(destroyed_block_result):
        for col, col_val in enumerate(row_val):
            if destroyed_block_result[row][col] == 1:
                for i in reversed(range(row)):
                    board[i+1][col] = board[i][col]
                    board[i][col] = '#'
    return board


def get_destroyed_block_num(board):

    destroyed_block_num = 0
    destroyed_block_result = [[0] * n for i in range(m)]

    for row, row_val in enumerate(board):
        for col, col_val in enumerate(row_val):
            if row < (m - 1) and col < (n - 1):
                if board[row][col] != '#' and board[row][col] == board[row + 1][col] \
                        and board[row][col] == board[row][col + 1] and board[row][col] == board[row + 1][col + 1]:
                    if destroyed_block_result[row][col] == 0:
                        destroyed_block_result[row][col] = 1
                        destroyed_block_num += 1
                    if destroyed_block_result[row + 1][col] == 0:
                        destroyed_block_result[row + 1][col] = 1
                        destroyed_block_num += 1
                    if destroyed_block_result[row][col + 1] == 0:
                        destroyed_block_result[row][col + 1] = 1
                        destroyed_block_num += 1
                    if destroyed_block_result[row + 1][col + 1] == 0:
                        destroyed_block_result[row + 1][col + 1] = 1
                        destroyed_block_num += 1

    board = make_board_destroyed(board, destroyed_block_result)
    if destroyed_block_num != 0:
        destroyed_block_num += get_destroyed_block_num(board)
    return destroyed_block_num


destroyed_block_num = get_destroyed_block_num(board)
print(destroyed_block_num)
