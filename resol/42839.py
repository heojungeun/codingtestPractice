def solution(numbers):
    from itertools import permutations
    answer = 0
    ns = []
    strnum = [x for x in numbers]
    for r in range(1,len(strnum)+1):
        tmp = [int("".join(x)) for x in list(permutations(strnum, r))]
        ns.extend(tmp)
    ns = set(ns)
    for x in ns:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            if x > 1:
                answer += 1
    return answer


num = "17"
print(solution(num))
