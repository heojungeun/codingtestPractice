import re
def solution(inputString):
    answer = -1
    st = []
    cnt = 0
    for x in inputString:
        a = isit(x)
        if a:
            if not st and a==1:
                st.append(x)
            elif not st and a==2:
                return -1
            elif a==1:
                st.append(x)
            else:
                if rever(x) in st:
                    st.pop(st.index(rever(x)))
                    cnt += 1
                else:
                    return -1
    if len(st) != 0:
        return -1
    return cnt

def isit(q):
    if q == "(" or q == "{"  or q == "["  or q == "<" :
        return 1
    elif q==")"or q=="}"or q == "]"or q==">":
        return 2
    return 0
def rever(s):
    if s=="}":
        return "{"
    if s==")":
        return "("
    if s=="]":
        return "["
    if s==">":
        return "<"


istr = "(Hello, (world!)"
print(solution(istr))