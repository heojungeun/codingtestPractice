def solution1(lines):
    from datetime import datetime, timedelta
    stime, etime = [], []
    for l in lines:
        tmp = l.split()
        # datetime fromisoformat 형식에 맞춰 yyyy-mm-ddTHH:mm:ss
        et = datetime.fromisoformat("".join(tmp[0]+'T'+tmp[1]))
        dur = timedelta(seconds=float(tmp[2][:-1])) # fff 형식으로 들어감
        etime.append(et)
        stime.append(et-dur+timedelta(seconds=0.001))
    total = stime + etime
    sec = timedelta(seconds=1)
    max_ = 0
    for t in total:
        res = 0
        for st, eti in zip(stime, etime):
            # 1초 섹션 안에서 시작되거나 끝난 로그
            if t <= eti < t+sec or t <= st < t+sec:
                res += 1
            elif st <= t and t + sec <= eti:
                # 1초 섹션안에 포함되어있지만 시작과 끝이 바깥에 있는 경우
                res += 1
        if max_ < res:
            max_ = res
    return max_

def solution(lines):
    S, E = [], []
    totalLines = 0
    for l in lines:
        totalLines += 1
        (d,s,t) = l.split(" ")

        t = float(t[:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm)*60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds-t+0.001)
    S.sort()
    cur, max_ = 0,0
    idxe, idxs = 0,0
    while (idxe < totalLines) and (idxs < totalLines):
        if S[idxs] < E[idxe]:
            cur += 1
            max_ = max(cur, max_)
            idxs += 1
        else:
            cur -= 1
            idxe += 1
    return max_


lis =["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lis))