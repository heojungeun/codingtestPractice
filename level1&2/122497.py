# def solution(numbers, target):
#     if not numbers and target==0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:],target-numbers[0])+solution(numbers[1:],target+numbers[0])
#
# n = [1,1,1,1,1]
# tar = 3
# print(solution(n,tar))

def solution(numbers):
    from itertools import permutations
    tmp = []
    for i in range(1,len(numbers)+1):
        tmp += list(permutations(list(numbers),i))
    setn = set()
    for x in tmp:
        setn.add(int("".join(x)))
    answer = 0
    for x in setn:
        if x < 2:
            continue
        for i in range(2,x):
            if x % i==0:
                break
        else:
            answer += 1
    return answer

n = "234"
print(solution(n))