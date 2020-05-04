# 가장 먼 노드
def solution1(n, edge):
    answer = 0
    gp = {}
    visited = {}
    for i in range(n+1):
        gp[i] = set()
        visited[i] = -1
    for x in edge:
        n1, n2 = x
        gp[n1].add(n2)
        gp[n2].add(n1)
    bfs(gp,1,visited)
    visitvalue = visited.values()
    for value in visitvalue:
        if value == max(visitvalue):
            answer += 1
    return answer

def bfs(gp, start, visit):
    from collections import deque
    cnt = 0
    q = deque([[start,cnt]])
    while q:
        value = q.popleft()
        v = value[0]
        cnt = value[1]
        if visit[v] == -1:
            visit[v] = cnt
            cnt += 1
            for e in gp[v]:
                q.append([e,cnt])

def solution(n, edge):
    from collections import deque
    gp = [[] for _ in range(n)]
    dist = [0 for _ in range(n)]
    visited = [-1 for _ in range(n)]
    q = deque([0])
    visited[0] = 1
    for (a,b) in edge:
        gp[a-1].append(b-1)
        gp[b-1].append(a-1)
    while q:
        i = q.popleft()
        for j in gp[i]:
            if visited[j]==-1:
                visited[j] = 1
                q.append(j)
                dist[j] = dist[i] + 1
    dist.sort(reverse=True)
    return dist.count(dist[0])

nodes = 6
edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(nodes,edges))