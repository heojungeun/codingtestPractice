def solution(board):
    h = len(board)
    w = len(board[0])
    maxb = -1
    for x in board:
        if 1 in x:
            maxb = 0
            break
        else:
            maxb = -1
    if maxb == -1:
        return 0
    for i in range(1,h):
        for j in range(1,w):
            if board[i][j] == 0:
                continue
            tmp = min(board[i-1][j-1],board[i-1][j],board[i][j-1]) + 1
            board[i][j] = tmp
            if maxb < tmp:
                maxb = tmp
    if maxb == 0:
        return 1
    return maxb**2

b= [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(b))