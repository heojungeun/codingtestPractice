def solution(numbers, target):
    cnt = 0
    lenn = len(numbers)
    def recur(idx=0):
        if idx < lenn:
            recur(idx+1)
            numbers[idx] *= -1
            recur(idx+1)
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1
    recur()
    return cnt

def sol(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return sol(numbers[1:],target-numbers[0])+sol(numbers[1:],target+numbers[0])

n = [1,1,1,1,1]
tar = 3
print(sol(n,tar))