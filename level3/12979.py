def solutionFail(n, stations, w):
    answer = 0
    prev = 1
    standard = 2*w+1
    for s in stations:
        tmp = s-w-prev
        if standard > tmp:
            answer += 1
        else:
            q, r = divmod(tmp, standard)
            if r==0:
                answer += q
            else:
                answer += q+1
        prev = s+w+1
    return answer

def solution(n, stations, w):
    answer = 0
    snum = []
    st = 0
    lens = len(stations)
    for i in range(lens):
        end = stations[i]-w-1
        snum.append(end-st)
        st = stations[i]+w
        if st > n : break
        if lens-1 == i:
            snum.append(n-st)
    for p in snum:
        q, r = divmod(p,w*2+1)
        if r:
            answer += q+1
        else:
            answer += q
    return answer

def solution1(n, stations, w):
    answer = 0
    idx = 0
    loc = 1
    lens = len(stations)
    while loc <= n:
        if idx < lens and stations[idx]-w <= loc:
            loc = stations[idx]+w+1
            idx += 1
        else:
            loc += 2*w+1
            answer += 1
    return answer
num = 11
sta = [4,11]
w_ = 1
print(solution1(num,sta,w_))