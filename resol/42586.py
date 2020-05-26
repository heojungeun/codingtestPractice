def solution(p, s):
    answer = []
    stack = []
    rel = [-((pro-100)//spe) for pro, spe in zip(p,s)]
    for x in rel:
        if not stack or stack[0]>=x:
            stack.append(x)
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(x)
    if stack:
        return answer+[len(stack)]
    return answer

pr = [93,30,55]
sp = [1,30,5]
print(solution(pr,sp))