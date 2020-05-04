def solution(bl, w, tw):
    answer = 0
    q = []
    qsize = 0
    for x in tw:
        while True:
            if not q:
                q.append(x)
                qsize += x
                answer += 1
                break
            elif bl == len(q):
                # answer += 1
                qsize -= q.pop(0)
            else:
                if w < qsize+x:
                    answer += 1
                    q.append(0)
                else:
                    answer += 1
                    q.append(x)
                    qsize += x
                    break
    return answer + bl

b,we = 100, 100
twe = [10]
print(solution(b,we,twe))