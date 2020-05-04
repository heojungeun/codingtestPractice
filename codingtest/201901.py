from collections import Counter
def solution(N, stages):
    users = len(stages)
    ansdic = {}

    for i in range(1,N+1):
        if users != 0:
            tmp = stages.count(i)
            ansdic[i] = tmp / users
            users -= tmp
        else:
            ansdic[i] = 0.0

    return sorted(ansdic, key=lambda x: ansdic[x], reverse= True)

n = 4
s = [4,4,4,4,4]
print(solution(n,s))