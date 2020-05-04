def solution(nums):
    from itertools import combinations
    answer = 0
    nums.sort()
    plist = primes(sum(nums[-3:]))
    for x in list(combinations(nums,3)):
        if sum(x) in plist:
            answer += 1
    return answer

def primes(n):
    seive = [False,False] + [True]*(n-1)
    for k in range(2, int(n**0.5 + 1.5)):
        if seive[k]:
            seive[k*2::k] = [False] * ((n-k) // k)
    return [x for x in range(n+1) if seive[x]]

def sol(nums):
    from itertools import combinations as cb
    answer = 0
    for x in cb(nums,3):
        sumx = sum(x)
        for i in range(2,sum(x)):
            if sumx % i == 0:
                break
        else:
            answer += 1
    return answer

ns = [1,2,7,6,4]
print(solution(ns))