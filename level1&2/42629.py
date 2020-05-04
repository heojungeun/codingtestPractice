def solution(stock, dates, supplies, k):
    import heapq
    answer, idx = 0, 0
    hq = []
    lend = len(dates)
    while stock<k:
        for i in range(idx, lend):
            if stock < dates[i]:
                break
            heapq.heappush(hq, -supplies[i])
            idx += 1
        stock += heapq.heappop(hq)*(-1)
        answer += 1
    return answer

stk = 4
dts = [4,10,15]
sp = [20,5,10]
k = 30
print(solution(stk,dts,sp,k))