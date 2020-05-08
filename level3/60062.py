#외벽 점검
def solution(n, weak, dist):
    from itertools import permutations
    lenw = len(weak)
    lend = len(dist)
    for i in range(lenw):
        weak.append(weak[i]+n)
    answer = lend + 1 # 최대 친구 수 + 계산 불가
    for i in range(lenw):
        # 시작 점 정하기
        stpoint = [weak[j] for j in range(i, i+lenw)]
        # 친구 순서 정하기, 모든 순서 탐색
        candi = permutations(dist, lend)
        for order in candi:
            f_idx, cnt = 0,1
            possible_check_len = stpoint[0] + order[f_idx]
            for idx in range(lenw):
                # 확인가능 최대 거리를 넘을 경우
                if stpoint[idx] > possible_check_len:
                    # 다음 친구 투입
                    cnt += 1
                    if cnt > len(order):
                        break
                    f_idx += 1
                    possible_check_len = stpoint[idx] + order[f_idx]
            answer = min(answer, cnt)
    if answer > lend:
        return -1
    return answer

num = 12
wk = [1,5,6,10]
dt = [1,2,3,4]
print(solution(num,wk,dt))