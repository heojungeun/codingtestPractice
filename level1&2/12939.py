def solution(s):
    s = s.split(" ")
    s = [int(x) for x in s]
    return str(min(s)) + " " + str(max(s))

st = "1 2 3 4"
print(solution(st))