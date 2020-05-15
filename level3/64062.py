def solutionFail(stones, k):
    answer = 0
    lens = len(stones)
    mins = min(stones)
    stones = [i - mins for i in stones]
    answer += mins
    while True:
        for i in range(lens):
            if stones[i] == 0:
                if stones[i:i+k].count(0)==k:
                    return answer
            else:
                stones[i] -= 1
        answer += 1
    return answer

def solution(stones,k):
    left = 1 # 최소 1명
    right = max(stones) + 1 # 최고값 + 1
    while left < right-1:
        mid = (left + right) // 2
        if check(k, stones, mid):
            left = mid
        else:
            right = mid
    return left

def check(k, sto, mid):
    a = 0
    for s in sto:
        if s-mid < 0: # 돌이 이 사람 수를 견뎌내지 못할 때
            a += 1
        else: # 연속적으로 k개가 되기전 견딜 수 있으면 0으로 초기화
            a = 0
        if a >= k: # k개 이상이면 false 반환
            return False
    return True

st = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k_ = 3
print(solution(st,k_))