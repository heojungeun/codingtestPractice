import math
from queue import PriorityQueue
def solution(N, road, K):
    answer = 0
    dist = dij(road,N)
    for d in dist:
        if d <= K:
            answer += 1
    return answer

def dij(r, n):
    dist = [math.inf for i in range(n+1)]
    r.sort()
    pq = PriorityQueue()
    pq.put([0,1]) # [ cost, here ]
    dist[1] = 0
    while not pq.empty():
        cost, here = pq.get()
        if cost > dist[here]: continue
        for i in range(len(r)):
            if r[i][0] == here:
                there, nextc = r[i][1], r[i][2] + cost
                if nextc < dist[there]:
                    dist[there] = nextc
                    pq.put([nextc, there])
            elif r[i][1] == here:
                there, nextc = r[i][0], r[i][2] + cost
                if nextc < dist[there]:
                    dist[there] = nextc
                    pq.put([nextc, there])
    return dist

import heapq
def solution1(N,road,K):
    answer = 0
    dist = [math.inf for _ in range(N+1)]
    adj = [[] for row in range(N+1)]
    visited = [False for _ in range(N+1)]

    for fr, to, c in road:
        adj[fr].append((to, c))
        adj[to].append((fr, c))

    hpq = [(1,0)]
    while hpq:
        here, cost = heapq.heappop(hpq)
        if dist[here] <= cost:
            continue
        dist[here] = cost
        for there, c in adj[here]:
            if dist[here] + c <= dist[there]:
                heapq.heappush(hpq, (there, dist[here]+c))
    for i in range(N+1):
        if dist[i] <= K:
            answer += 1
    return answer


n = 5
r = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
k = 3
print(solution1(n,r,k))