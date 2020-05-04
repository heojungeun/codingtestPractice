def solution(s, n):
    answer = ''
    zord = ord('z')
    Zord = ord('Z')
    aord = ord('a')
    Aord = ord('A')
    for x in s:
        if x==' ':
            answer += " "
            continue
        xord = ord(x)
        if zord < xord + n and x.islower():
            answer += chr(aord-1+n-zord+xord)
        elif Zord < xord + n and x.isupper():
            answer += chr(Aord-1 + n - Zord + xord)
        else:
            answer += chr(ord(x)+n)
    return answer

st = "abc"
num = 25

print(solution(st,num))