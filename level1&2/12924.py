# 연속되는 수의 합
def solution(n):
    answer = 0
    maxn = n//2+1
    for i in range(1,maxn):
        tmp = i
        for j in range(i+1,maxn+1):
            tmp += j
            if tmp > n:
                break
            if tmp==n:
                answer +=1
                break
    return answer+1

def sol(n):
    return len([i for i in range(1,n,2) if n % i == 0])

num = 3
print(solution(num))