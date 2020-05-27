def solution(arrangement):
    answer = 0
    stack = []
    arr = arrangement.replace("()", "*")
    for x in arr:
        if x == "*":
            answer += len(stack)
        else:
            if x=="(":
                stack.append(x)
            else:
                stack.pop()
                answer += 1
    return answer

def solution1(arr):
    answer = 0
    stack = 0
    a = arr.replace("()","*")
    for x in a:
        if x == "*":
            answer += stack
        elif x == "(":
            stack += 1
        else:
            stack -= 1
            answer += 1
    return answer

a_ = "()(((()())(())()))(())"
print(solution1(a_))