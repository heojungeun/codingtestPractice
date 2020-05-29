def solution(n, computers):
    answer = 0
    alist = {e: [] for e in range(n)}
    for i in range(n):
        x = computers[i]
        if x.count(1) != 1:
            for j in range(n):
                if i != j and x[j] == 1:
                    alist[i].append(j)
        else:
            alist.pop(i, None)
            answer += 1
    group = []
    for k in alist.keys():
        if k not in group:
            v = dfs(alist, k)
            group.extend(v.keys())
            answer += 1
    return answer

def dfs(graph, root):
    visited = {}
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited.keys():
            visited[n] = True
            for x in graph[n]:
                if x not in visited.keys():
                    stack.append(x)
    return visited


n_ = 3
comp_ = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n_, comp_))
