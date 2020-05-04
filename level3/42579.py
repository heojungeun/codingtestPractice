def solution(genres, plays):
    answer,order = [],[]
    pdict = {} # 총 재생횟수
    idict = {} # 플레이횟수, 고유번호
    cnt = 0
    max = 0
    for (g,p) in zip(genres,plays):
        pdict[g] = pdict.get(g,0) + p
        idict[g] = idict.get(g,[]) + [(p, cnt)]
        cnt += 1
    order = sorted(pdict.items(), key=lambda x:x[1] ,reverse=True)
    for od in order:
        o = od[0]
        idict[o].sort(key=lambda x:(-x[0],x[1]))
        if len(idict[o])==1:
            answer.append(idict[o][0][1])
        else:
            answer.append(idict[o][0][1])
            answer.append(idict[o][1][1])
    return answer

gr = ["classic", "pop", "classic", "classic", "pop"]
ps = [500, 600, 150, 800, 2500]
print(solution(gr,ps))