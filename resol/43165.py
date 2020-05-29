def solution(numbers, target):
    if not numbers and target==0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

def solution1(numbers, target):
    from itertools import product
    line = [(x, -x) for x in numbers]
    sums = list(map(sum, product(*line)))
    return sums.count(target)

def solution2(numbers, target):
    return dfs(numbers, 0, 0, target)

def dfs(nums, i, n, t):
    ans = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ans += dfs(nums, i+1, n+nums[i], t)
    ans += dfs(nums, i+1, n-nums[i], t)
    return ans

n_ = [1,1,1,1,1]
t_ = 3
print(solution1(n_, t_))