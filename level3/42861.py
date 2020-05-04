#kruskal
def solution(n, costs):
    answer = 0
    parent = {}
    rank = {}
    for v in range(n):
        parent[v] = v
        rank[v] = 0
    mst = []
    costs.sort(key= lambda x:x[2])
    for edge in costs:
        v, u, w = edge
        if find(v,parent) != find(u,parent):
            union(v, u, parent, rank)
            mst.append(edge)
    for x in mst:
        answer += x[2]
    return answer

def find(v, p):
    if p[v] != v:
        p[v] = find(p[v],p)
    return p[v]

def union(v, u, p, r):
    root1 = find(v,p)
    root2 = find(u,p)
    if r[root1] > r[root2]:
        p[root2] = root1
    else:
        p[root1] = root2
        if r[root1] == r[root2]:
            r[root2] += 1
num= 4
csts =[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(num,csts))