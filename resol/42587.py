def solution(priorities, location):
    from collections import deque
    answer = 0
    arr = sorted(priorities, reverse=True)
    idx = 0
    dep = deque(priorities)
    lend = len(dep)
    while True:
        if arr[idx] == dep[0]:
            answer += 1
            dep.popleft()
            lend -= 1
            idx += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            dep.append(dep.popleft())
            if location == 0:
                location = lend-1
            else:
                location -= 1
    return answer

p_ = [2,1,3,2]
l_ = 2
print(solution(p_,l_))