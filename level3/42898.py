def solution(m, n, puddles):
    answer = 0
    mat = [[1 for _ in range(m)] for row in range(n)]
    for (x,y) in puddles:
        mat[y-1][x-1] = 0
        if x==1:
            for i in range(n-y):
                mat[n-i-1][0] = 0
        elif y==1:
            for i in range(m-x):
                mat[0][m-i-1] = 0
    for x in range(1,m):
        for y in range(1,n):
            if mat[y][x] != 0:
                mat[y][x] = mat[y-1][x] + mat[y][x-1]
    return mat[n-1][m-1] % 1000000007

w = 4
h = 3
pdds =[[2,2]]
print(solution(w,h,pdds))