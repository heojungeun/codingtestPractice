# 괄호 변환
import sys
sys.setrecursionlimit(10000)
from collections import Counter

def solution(p):
    answer = ''
    if not p:
        return ''
    answer = bigsp(p)
    return answer

def bigsp(string):
    if not string:
        return ''
    u, v = strsplit(string)
    tmp = ''
    if iscomp(u) == 1:
        v = u+bigsp(v)
    else:
        tmp += '('
        tmp += bigsp(v)
        tmp += ')'
        tmp += chg(u[1:-1])
        v = tmp
    return v
def chg(s):
    tmp = ''
    if not s:
        return ''
    for x in s:
        if x == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp
def strsplit(s):
    for i in range(0,len(s),2):
        c = list(Counter(s[:i]).items())
        if len(c) < 2:
            continue
        else:
            if c[0][1] == c[1][1]:
                return s[:i], s[i:]
    return s,''

def iscomp(s):
    st = []
    for x in s:
        if x==')':
            if not st:
                return -1
            elif st[-1]=='(':
                st.pop()
            else:
                return -1
        else:
            st.append(x)
    return 1

pp = ")("
print(solution(pp))