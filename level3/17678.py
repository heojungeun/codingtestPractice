def solution(n, t, m, timetable):
    ttint = [int(tb[:2])*60 + int(tb[3:])for tb in timetable]
    ttint.sort()
    last = 540 + (n-1)*t # 9:00 -> 540
    for i in range(n):
        if len(ttint) < m: # 전부 수용가능하다면 제일 늦게 가도됨
            return "%02d:%02d" % (last//60, last%60)
        if i == n-1: # 마지막 차라면
            if ttint[0] > last: # 마지막 차시간보다 크다면
                return "%02d:%02d" % (last // 60, last % 60)
            last = ttint[m-1] -1 # 수용가능인원 순서보다 1앞서기
            return "%02d:%02d" % (last // 60, last % 60)
        busarrive = 540 + i * t
        for j in range(m-1,-1,-1): # 이번 버스도착시간에 탈 크루들 삭제하기
            if ttint[j] <= busarrive:
                del ttint[j]

n_ = 2
t_ = 10
m_ = 2
tt = ["09:10", "09:09", "08:00"]
print(solution(n_,t_,m_,tt))