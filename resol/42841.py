def solution(baseball):
    from itertools import permutations
    answer = 0
    res = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for r in res:
        for n, s, b in baseball:
            n = str(n)
            strike, ball = 0, 0
            for i in range(3):
                for j in range(3):
                    if n[i] == str(r[j]) and i == j:
                        strike += 1
                    elif n[i] == str(r[j]) and i != j:
                        ball += 1
            if s != strike or b != ball:
                break
        else:
            answer += 1
    return answer


bb = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(bb))
