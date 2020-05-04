import re
from collections import Counter


def solution(s):
    answer = []
    s = s[2:-2]
    if "," not in s:
        return [int(s)]
    s = [x.split(',') for x in s.split("},{")]
    s.sort(key=len)
    for x in s:
        for y in x:
            if int(y) not in answer:
                answer.append(int(y))
    return answer

def sol(s):
    s = Counter(re.findall('\d+',s))
    return [int(x[0]) for x in sorted(s.items(), key= lambda x:x[1],reverse=True)]

strtuple = 	"{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(sol(strtuple))