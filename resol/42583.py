def solution(bl, w, tw):
    from collections import deque
    answer = 0
    q = deque([0]*bl)
    tw_copy = deque(tw)
    sumq = 0
    while q:
        answer += 1
        sumq -= q.popleft()
        if tw_copy:
            if sumq+tw_copy[0] <= w:
                tmp = tw_copy.popleft()
                q.append(tmp)
                sumq += tmp
            else:
                q.append(0)
    return answer

bl_ = 2
wg = 10
tw_ = [7,4,5,6]
print(solution(bl_,wg,tw_))