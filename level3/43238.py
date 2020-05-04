# 입국심사
def solution(n, times):
    answer = 0
    lent = len(times)
    left, right = 1, max(times)*n
    while left<=right:
        people = 0
        mid = (left+right)//2
        for time in times:
            people += mid//time
            if people >= n:
                answer = mid
                right = mid-1
                break
        else: # 인원수가 모자른 경우
            left = mid+1
    return answer

num = 6
ts = [7,10]
print(solution(num,ts))