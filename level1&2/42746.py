def solution(numbers):
    p = [str(x) for x in numbers]
    strp = sorted(p, reverse=True, key=lambda x:x*3)
    return str(int("".join(strp)))
# str(int() 이유는 0이 앞에 있을 가능성을 배제하기 위해서

n = [3, 30, 34, 5, 9]
print(solution(n))