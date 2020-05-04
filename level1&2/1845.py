def solution(nums):
    answer = 0
    setmon = list(set(nums))
    lens, lenn = len(setmon), len(nums)
    if lens < lenn/2:
        answer = lens
    else:
        answer = lenn//2
    return answer

def sol(nums):
    return min(len(set(nums)), len(nums)//2)

ns = [3,3,3,2,2,4]
print(solution(ns))