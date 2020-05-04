def solution(citations):
    citations.sort()
    print(citations)
    lenc = len(citations)
    answer = 0
    for i in range(lenc):
        if citations[i]>= lenc-i:
            return lenc-i
    return answer

def solution1(citations):
    citations.sort(reverse=True)
    lenc = len(citations)
    for i in range(lenc):
        if i >= citations[i]:
            return i
    return 0

cita = [4,3,3,3,3]
print(solution1(cita))