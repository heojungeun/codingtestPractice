def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for x,y in zip(A,B):
        answer += x*y
    return answer

a = [1,4,2]
b = [5,4,4]
print(solution(a,b))