def solution(s):
    import re
    answer = []
    if ',' not in s:
        return [int(s[2:-2])]
    tulist = []
    p = re.compile("\d{1,6}")
    for e in s[1:-1].split("},"):
        tulist.append(p.findall(e))
    tmp = sorted(tulist, key=len)
    for x in tmp:
        if not answer:
            answer.append(int(x.pop()))
        else:
            for y in x:
                inty = int(y)
                if inty not in answer:
                    answer.append(inty)
    return answer

s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{123}}"
s3 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
s4 = "{{20,111},{111}}"
print(solution(s4))