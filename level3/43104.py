def solution(N):
    a,b= 4,6
    if N==1:
        return a
    for _ in range(2,N):
        a, b = b, a+b
    return b

def solution1(N):
    arr = [1,1]
    for i in range(2,N+1):
        arr.append(arr[-1]+arr[-2])
    return arr[-1]*2+arr[-2]*2
n = 3
print(solution1(n))