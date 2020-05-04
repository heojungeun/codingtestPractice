def solution(n):
    answer = 0
    if (n**0.5).is_integer():
        answer = ((n**0.5)+1)**2
    else:
        answer= -1
    return int(answer)

num = 3
print(solution(num))