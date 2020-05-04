def solution1(n):
    answer = 0
    for x in range(2,n+1):
        flag = 0
        for y in range(2,x+1):
            if x % y == 0 and x != y:
                flag = 1
                break
        if flag == 0:
            answer += 1
    return answer

def solution(n):
    seive = [False, False] + [True]*(n-1)
    for x in range(2,int(n**0.5 + 1.5)):
        if seive[x]:
            seive[x*2::x] = [False] * ((n-x)//x)
    return seive.count(True)

num = 10
print(solution(num))