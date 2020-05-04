def solution(scoville, K):
    import heapq
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
            cnt += 1
        except IndexError:
            return -1
    return cnt

scv = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scv, k))