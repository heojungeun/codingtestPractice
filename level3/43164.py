from collections import defaultdict
def solution(tickets):
    #fg = defaultdict(list)
    # for x in tickets:
    #     st, des = x
    #     fg[st].append(des)
    fg = dict()
    for (st, end) in tickets:
        fg[st] = fg.get(st, []) + [end]
    for x in fg:
        fg[x].sort(reverse=True)
    st, path = ["ICN"],[]
    while st:
        tmp = st[-1]
        if tmp not in fg or len(fg[tmp]) == 0:
            path.append(st.pop())
        else:
            st.append(fg[tmp].pop())
    return path[::-1]

tks = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
ttt = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(ttt))