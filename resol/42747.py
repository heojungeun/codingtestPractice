def solution(citations):
    answer = 0
    lenc = len(citations)
    citations.sort()
    for i in range(lenc):
        if citations[i] >= lenc-i:
            return lenc - i
    return answer
c = [3,0,6,1,5]
print(solution(c))