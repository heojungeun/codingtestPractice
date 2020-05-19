def solution(A, B):
    answer = 0
    ta = sorted(A)
    tb = sorted(B)
    for i in ta:
        for j in tb:
            if i < j:
                answer += 1
                tb.remove(j)
                break
    return answer

def solution1(A,B): # 이게 더 빠름
    from collections import deque
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    while A:
        if A[-1] < B[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            A.pop()
            B.popleft()
    return answer
a = [5,1,3,7]
b = [2,2,6,8]
print(solution1(a,b))