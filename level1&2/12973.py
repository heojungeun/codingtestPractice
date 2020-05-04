def solution(s):
    answer = 0
    st = []
    for x in s:
        if not st or st[-1] != x:
            st.append(x)
        elif st[-1]==x:
            st.pop()
    if s:
        return 0
    return 1

string = "baabaa"
print(solution(string))