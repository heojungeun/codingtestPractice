# 한 단어를 한 글자만 바꿔서 최종 단어에 도달하기
def solution(begin, target, words):
    import re
    if target not in words:
        return 0
    wdic = {}
    lenb = len(begin)
    words = [begin] + words
    for x in words:
        wdic[x] = set()
        for idx in range(lenb):
            tmp = x[:idx] + "." +x[idx+1:]
            for y in words:
                if x == y:
                    continue
                if re.match(tmp,y):
                    wdic[x].add(y)
    answer = bfs2(wdic,begin,target)
    return answer

def bfs2(gp,node,tar):
    st = [node]
    cnt = 0
    visit = {}
    visit[node]=True
    while st:
        tmp = st.pop()
        if tmp==tar:
            return cnt
        for x in gp[tmp]:
            if x in visit:
                continue
            visit[x] = True
            st.append(x)
        cnt += 1
    return cnt
b="hit"
tar = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(b,tar,w))