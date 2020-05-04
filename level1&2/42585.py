def solution(arrangement):
    answer = 0
    st = []
    arr1 = arrangement.replace("()","*")
    for x in arr1:
        if x == "*":
            answer += len(st)
        elif x == "(":
            st.append(x)
        else:
            st.pop()
            answer += 1
    return answer

arr = "()(((()())(())()))(())"
print(solution(arr))