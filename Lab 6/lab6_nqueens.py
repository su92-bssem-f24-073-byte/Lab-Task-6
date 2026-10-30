N = 4
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def solve_nqueens(board=[], row=0):
    if row == N:
        return board   
    for col in range(N):
        if is_safe(board, row, col):
            board.append(col)
            result = solve_nqueens(board, row + 1)
            if result:
                return result
            board.pop()           
    return None
solution = solve_nqueens()
print("N-Queens Solution (Column positions for each row):", solution)