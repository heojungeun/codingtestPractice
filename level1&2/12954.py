def solution(x, n):
    answer = []
    if x==0:
        return [0]*n
    for i in range(0,n*x,x):
        answer.append(x+i)
    return answer

a, b = -4,2
print(solution(a,b))