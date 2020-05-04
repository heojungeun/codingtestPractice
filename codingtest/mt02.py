K = int(input())
answer = []
for i in range(K):
    M, N = map(int,input().split())
    matrix = []
    for x in range(M):
        matrix.append(list(map(int,input().split())))
    for x in range(M-1):
        for y in range(N-1):
            if matrix[x][y]>0 and matrix[x+1][y+1]>0 and matrix[x+1][y]>0 and matrix[x][y+1]>0:
                matrix[x][y] = matrix[x + 1][y + 1] = matrix[x + 1][y] = matrix[x][y + 1] = 2
    flag = 0
    for x in matrix:
        for y in x:
            if y==1:
                flag=1
                break
    if flag==0:
        answer.append('YES')
    else:
        answer.append('NO')

for x in answer:
    print(x)