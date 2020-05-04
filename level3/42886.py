# greedy 저울
def solutionNo(weight):
    from itertools import combinations
    answer = 0
    listp = []
    for i in range(len(weight)):
        listp += list(combinations(weight,i))
    setp = set(listp)
    listp = set()
    for x in setp:
        sumx = sum(x)
        listp.add(sumx)
    maxp = max(listp)
    for i in range(1,maxp):
        if i not in listp:
            answer = i
            break
    else:
        answer = maxp + 1
    return answer

def solution(weight):
    answer = 1
    weight.sort()
    for w in weight:
        if answer >= w:
            answer += w
        else:
            break
    return answer

w = [3, 1, 6, 2, 7, 30, 1]
print(solution(w))