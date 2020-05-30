def solution(tickets):
    from collections import defaultdict
    answer = []
    graph = defaultdict(list)
    N = len(tickets)
    for s, d in tickets:
        graph[s].append(d)
        graph[s].sort()

    return dfs(graph, N, "ICN", ["ICN"])


def dfs(g, n, k, f):
    if len(f) == n + 1:
        return f
    for idx, cty in enumerate(g[k]):
        g[k].pop(idx)

        tmp = f[:]
        tmp.append(cty)

        ret = dfs(g, n, cty, tmp)
        g[k].insert(idx, cty)

        if ret:
            return ret


def solution1(tickets):
    graph = {}
    for s, d in tickets:
        graph[s] = graph.get(s, []) + [d]
    for g in graph:
        graph[g].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in graph or not graph[top]:
            path.append(stack.pop())
        else:
            stack.append(graph[top].pop())
    return path[::-1]


t_ = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution1(t_))
