def solution(begin, target, words):
    arr = [begin] + words
    lenw = len(words[0])
    graph = {e: [] for e in arr}
    for x in graph:
        for y in arr:
            if x != y and check(x, y, lenw):
                graph[x].append(y)
    minc = bfs(graph, begin, target)
    return minc

def check(a, b, size):
    cnt = 0
    for i in range(size):
        if a[i] != b[i]:
            if cnt == 1:
                return False
            else:
                cnt += 1
    return True

def bfs(g, b, t):
    from collections import deque
    visited = {b: 0}
    deq = deque([b])
    while deq:
        tmp = deq.popleft()
        for next in g[tmp]:
            if next not in visited:
                visited[next] = visited[tmp] + 1
                deq.append(next)
    return visited.get(t, 0)



b_ = "hit"
t_ = "cog"
w_ = ["hot", "dot", "dog", "lot", "log"]
print(solution(b_, t_, w_))
