def solution(x):
    if x < 10:
        return True
    arr = [int(i) for i in str(x)]
    if x % sum(arr)==0:
        return True
    else:
        return False

num = 12
print(solution(num))