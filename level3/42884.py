def solutionNo(routes):
    answer = 0
    stidx, endidx = 30001, -30001
    for x in routes:
        st, ed = x[0],x[1]
        if st < stidx:
            stidx = st
        if ed > endidx:
            endidx = ed
    stdarr = [""] * (endidx-stidx+1)
    cnt = 0
    for x in routes:
        cntidx = str(cnt)
        st, ed = x[0]-stidx, x[1]-stidx
        for i in range(st,ed+1):
            stdarr[i] += cntidx
        cnt += 1
    import re
    print(stdarr)

    return answer

def solution(routes):
    answer = 0
    prev = -30000
    routes.sort(key= lambda x:x[1])
    for r in routes:
        if prev < r[0]:
            answer += 1
            prev = r[1]
    return answer

rtes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(rtes))