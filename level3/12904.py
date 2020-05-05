def solution(s):
    answer = 0
    lens = len(s)
    for i in range(0, lens):
        for j in range(1, lens+1-i):
            orin = s[i:i+j]
            rev = orin[::-1]
            if orin == rev and j > answer:
                answer = j
    return answer

def solution1(s):
    for i in range(len(s),0,-1):
        for j in range(len(s)+1-i):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i

string = "abcdcba"
print(solution(string))