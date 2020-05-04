def solution(skill, skill_trees):
    answer = len(skill_trees)
    for ele in skill_trees:
        st = []
        for x in ele:
            if x in skill:
                st.append(x)
        for y in skill:
            if not st:
                break
            if st.pop(0) != y:
                answer -= 1
                break
    return answer

sk = "CBD"
skt = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(sk,skt))