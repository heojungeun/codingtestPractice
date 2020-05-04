# 카카오 매트릭스 키 맞추기
def solution(key, lock):
    answer = True
    M, N = len(key), len(lock)
    BGsize = N+2*M-2
    cstart = M-1 # 중심 시작부분
    cend = cstart + N
    for i in range(4):
        for x in range(BGsize-(M-1)):
            for y in range(BGsize-(M-1)):
                res = addkeylock(BGsize,key,lock,M,N,x,y,cstart)
                if res:
                    return True
        key = trans(key,M)
    return False

def trans(mat, n):
    tmp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-1-i] = mat[i][j]
    return tmp

def addkeylock(bgsize,_key,_lock,_m,_n,sx,sy,cs):
    bg = [[0]*bgsize for i in range(bgsize)]
    for x in range(_m):
        for y in range(_m):
            bg[sx+x][sy+y] = _key[x][y]
    for x in range(_n):
        for y in range(_n):
            bg[cs+x][cs+y] += _lock[x][y]
            if bg[cs+x][cs+y]!=1:
                return False
    return True

k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(k,l))