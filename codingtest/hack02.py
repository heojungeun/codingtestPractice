def solution(id_list, k):
    from collections import Counter
    answer = 0
    cntid = []
    for x in id_list:
        cntid += list(set(x.split(" ")))
    counter = Counter(cntid)
    for key, v in counter.items():
        if v >= k:
            answer += k
        else:
            answer += v
    return answer

idlistout = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
kout = 3
print(solution(idlistout,kout))