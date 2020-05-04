def solution(s):
    answer = False
    s = s.lower()
    if s.count('p') == s.count('y'):
        answer = True
    return answer

string= "Pyy"
print(solution(string))