def solution(n, works):
    import heapq
    if sum(works) <= n:
        return 0
    answer = 0
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)
    for i in range(n):
        m = heapq.heappop(works)
        if m >= 0:
            break
        m += 1
        heapq.heappush(works,m)
    return sum([w**2 for w in works])

num = 4
wks = [4,3,3]
print(solution(num,wks))