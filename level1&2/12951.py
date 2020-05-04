def solution(s):
    answer = ""
    s = s.lower().split(" ")
    for x in s:
        answer += x.capitalize() + " "
    return answer[:-1]

stj = "3people unFollowed me"
print(solution(stj))