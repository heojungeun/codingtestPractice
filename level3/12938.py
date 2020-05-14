def solution(n, s):
    if n > s: return [-1]
    answer = [s//n]*n
    for i in range(s%n):
        answer[i%n] += 1
    return sorted(answer)

n_ = 2
s_ = 9
print(solution(n_,s_))