from collections import deque
class node(object):
    def __init__(self, x=0,y=0,x2=1,y2=0, dist=0, state= True):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.dist = dist
        self.state = state # 가로 true, 세로 false
    def getxy(self):
        return self.x, self.y
    def getxy2(self):
        return self.x2, self.y2

def findNext(b, nd):
    N = len(b) - 1
    nxtdst = []
    x, y = nd.getxy()
    x2, y2 = nd.getxy2()
    dist = nd.dist + 1
    if nd.state:
        if x2 < N and b[y][x2 + 1]==0: # 오른쪽 이동 가능
            nxtdst.append(node(x+1,y,x2+1,y2,dist, True))
        if x > 0 and b[y][x - 1]==0:# 왼쪽 이동 가능
            nxtdst.append(node(x-1,y,x2-1,y2,dist,True))
        if y2 < N and b[y2+1][x]==0 and b[y+1][x+1]==0: # 아래 2칸 여유있음
            nxtdst.append(node(x, y+1, x+1, y+1, dist, True)) # 통째로 아래
            nxtdst.append(node(x, y, x, y+1, dist, False)) # 왼쪽 밑으로 회전
            nxtdst.append(node(x+1, y, x+1, y+1, dist, False)) # 오른쪽 밑으로 회전
        if y > 0 and b[y-1][x] == 0 and b[y-1][x+1]==0:
            nxtdst.append(node(x,y-1,x2,y2-1,dist,True))
            nxtdst.append(node(x,y-1,x,y,dist,False))
            nxtdst.append(node(x+1,y-1,x2,y2,dist,False))
    else:# 세로
        if y2 < N and b[y2+1][x2]==0:
            nxtdst.append(node(x, y + 1, x2, y2 + 1, dist, False))
        if y > 0 and b[y-1][x]==0:
            nxtdst.append(node(x, y - 1, x2, y2 - 1, dist, False))
        if x2 < N and b[y][x2+1]==0 and b[y+1][x2+1]==0:
            nxtdst.append(node(x + 1, y, x2 + 1, y2, dist, False))
            nxtdst.append(node(x, y, x2 + 1, y2 - 1, dist, True))
            nxtdst.append(node(x2, y2, x + 1, y + 1, dist, True))
        if x > 0 and b[y][x-1]==0 and b[y+1][x-1]==0:
            nxtdst.append(node(x - 1, y, x2 - 1, y2, dist, False))
            nxtdst.append(node(x - 1, y, x2, y2 - 1, dist, True))
            nxtdst.append(node(x - 1, y + 1, x2, y2, dist, True))
    return nxtdst

def solution(board):
    answer = 0
    N = len(board) - 1
    cur = node()
    q = deque([cur])
    visit = []
    while q:
        cur = q.popleft()
        if cur.getxy() == (N,N) or cur.getxy2() == (N,N):
            return cur.dist
        if (cur.getxy(), cur.getxy2()) not in visit:
            visit.append((cur.getxy(), cur.getxy2()))
            q.extend(findNext(board,cur))

    return answer

b = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(b))