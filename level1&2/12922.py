def solution(n):
    answer = ''
    arr = ['수','박']
    for x in range(n):
        answer += arr[x%2]
    return answer

print(solution(7))