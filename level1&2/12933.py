def solution(n):
    tmp = ""
    answer = [int(x) for x in str(n)]
    answer.sort(reverse=True)
    for x in answer:
        tmp += str(x)
    return int(tmp)

print(solution(118372))