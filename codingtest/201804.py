def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    D = [[0]*n for _ in range(m)]
    cnt = 0

    while True:
        flag = 0
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]!=" ":
                    D[i][j] = D[i][j + 1] = D[i + 1][j] = D[i + 1][j + 1] = 1
                    flag = 1
        if flag != 1:
            break
        for j in range(n):
            tmp = []
            for i in range(m):
                if D[i][j]==0:
                    tmp.append(board[i][j])
                else:
                    D[i][j]=0
                    cnt += 1
            for c in range(m):
                if len(tmp) < (m-c):
                    board[c][j] = " "
                else:
                    board[c][j] = tmp[c-m+len(tmp)]
    for i in board:
        for j in i:
            print(j, end=' ')
        print ()
    answer = cnt
    return answer


h = 6
w = 6
b = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(h,w,b))