def solution(n, computers):
    answer = 0
    graph = {}
    for i in range(n):
        graph[i] = [j for j in range(n) if computers[i][j]==1 and i!=j]
    for x in graph.values():
        if x:
            break
    else:
        # 전부 다 연결안된 경우
        return n
    while graph:
        idx = list(graph.keys())[0]
        v = dfs(graph,idx)
        if len(v)==n:
            return 1
        answer += 1
        for x in v.keys():
            del graph[x]
    return answer

def dfs(gp, stnode):
    visit = {}
    stlist = list()
    stlist.append(stnode)
    while stlist:
        node = stlist.pop()
        if node not in visit:
            visit[node] = True
            stlist.extend(gp[node])
    return visit

def solution1(n, cmps):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(cmps, visited, start):
        stlist = [start]
        while stlist:
            j = stlist.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(n):
                if cmps[j][i] == 1 and visited[i] == 0:
                    stlist.append(i)
    i = 0
    while 0 in visited:
        if visited[i]==0:
            dfs(cmps,visited,i)
            answer += 1
        i += 1
    return answer

num = 3
comp = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#comp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(solution(num,comp))