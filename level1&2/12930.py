def solution(s):
    answer = []
    lists = s.split(' ')
    for idx,x in enumerate(lists):
        arr = ''
        for i in range(len(x)):
            if i%2==0:
                arr += x[i].upper()
            else:
                arr += x[i].lower()
        answer.append(arr)
    return ' '.join(answer)

print(solution("try hello world"))