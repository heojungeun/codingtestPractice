def solutionNo(jobs):
    import heapq
    answer = 0
    prev = 0
    heap = []
    for x in jobs:
        heapq.heappush(heap, (x[1],x[0]))
    for i in jobs:
        work = heapq.heappop(heap)
        answer += work[0] + prev - work[1]
        prev = work[0] + prev
    answer //= len(jobs)
    return answer

def solution(jobs):
    import heapq
    answer = 0
    n = len(jobs)
    time, end, q = 0, -1, []
    cnt = 0
    while cnt < n:
        for i in jobs:
            if end < i[0] <= time:
                answer += (time - i[0]) # 요청이후 대기시간 저장
                heapq.heappush(q, i[1])
        if len(q)>0:
            answer += len(q) * q[0]
            end = time
            time += heapq.heappop(q)
            cnt += 1
        else:
            time += 1
    return answer//n

jbs = [[0, 3], [1, 9], [2, 6]]
print(solution(jbs))