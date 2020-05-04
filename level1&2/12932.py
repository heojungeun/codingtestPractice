def solution(n):
    answer = [int(x) for x in str(n)]
    answer.reverse()
    return answer

print(solution(12345))