def solution(N, number):
    answer = 0
    s = [set() for i in range(8)]
    for i, x in enumerate(s,start=1):
        x.add(int(str(N)*i))
    for i in range(1,8):
        for j in range(i):
            for x in s[j]:
                for y in s[i-j-1]:
                    s[i].add(x+y)
                    s[i].add(x-y)
                    s[i].add(x*y)
                    if y != 0:
                        s[i].add(x//y)
        if number in s[i]:
            return i+1
    return -1

def solution1(N, number):
    S = [0, {N}]
    for i in range(2,9):
        case_set = {int(str(N)*i)}
        for j in range(1, i//2+1):
            for x in S[j]:
                for y in S[i-j]:
                    case_set.add(x + y)
                    case_set.add(x - y)
                    case_set.add(y - x)
                    case_set.add(x * y)
                    if x != 0: case_set.add(x // y)
                    if y != 0: case_set.add(y // x)
        if number in case_set:
            return i
        S.append(case_set)
    return -1

n = 5
nb = 12
print(solution(n,nb))