def solution(phone_number):
    answer = ""
    for x in phone_number[:-4]:
        answer += '*'
    answer += phone_number[-4:]
    return answer

num = "4444"
print(solution(num))