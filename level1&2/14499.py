N,M,x,y,K = map(int,input().split())
m = []
for i in range(N):
    m.append(list(map(int,input().split())))
k = list(map(int,input().split()))
dice,tmp = [0]*6,[0]*6
dx,dy = (0,0,-1,1),(1,-1,0,0)
dim = [
    (2,0,5,3,4,1),
    (1,5,0,3,4,2),
    (4,1,2,0,5,3),
    (3,1,2,5,0,4)
]
for z in k:
    z -= 1 # 1~4 -> 0~3
    x += dx[z]
    y += dy[z]
    if x > N-1 or y > M-1 or x < 0 or y < 0:
        x -= dx[z]
        y -= dy[z]
        continue
    tmp = [j for j in dice]
    for j in range(6):
        dice[j] = tmp[dim[z][j]]
    num = m[x][y]
    if num == 0:
        m[x][y] = dice[5]
    else:
        dice[5] = num
        m[x][y] = 0
    print(dice[0])
