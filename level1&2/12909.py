def solution(s):
    stacks = []
    for x in s:
        if not stacks:
            if x == "(":
                stacks.append(x)
            else:
                return False
        elif x == "(":
            stacks.append(x)
        else:
            stacks.pop()
    if stacks:
        return False
    return True

def is_pair(s):
    x= 0
    for w in s:
        if x < 0:
            break
        if w=="(":
            x = x+1
        else:
            x = x-1
    return x==0

st = "()()"
print(is_pair(st))