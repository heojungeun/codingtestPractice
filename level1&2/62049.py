def solution(n):
    answer = [0]
    for x in range(n-1):
        answer = answer + [0] + [i^1 for i in answer[::-1]]
    return answer

num = 3
print(solution(num))