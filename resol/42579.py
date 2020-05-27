def solution(genres, plays):
    answer, order = [], {}
    sums = {}
    idx = 0
    for g, p in zip(genres,plays):
        order[g] = order.get(g, []) + [(p, idx)]
        sums[g] = sums.get(g,0) + p
        idx += 1
    res = sorted(sums.items(), key=lambda x : -x[1])
    for g, s in res:
        tmp = order[g]
        if len(tmp)==1:
            answer.append(tmp[0][1])
        else:
            order[g].sort(key= lambda x: (-x[0], x[1]))
            answer.append(order[g][0][1])
            answer.append(order[g][1][1])
    return answer

g_ = ["classic", "pop", "classic", "classic", "pop"]
p_ = [500, 600, 150, 800, 2500]
print(solution(g_, p_))