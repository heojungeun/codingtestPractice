import re
def solution(dartResult):
    answer = 0
    expdic = {'S':1, 'D':2, 'T':3}
    numarr = [1,1,1]
    starr =[1,1,1,1]
    darr = [1,1,1]
    str = re.findall('\d{1,2}[SDT][*#]?',dartResult)

    for i, x in enumerate(str):
        if x[-1] in '*#':
            if x[-1]== '*':
                starr[i] = 2
            elif x[-1]== '#':
                darr[i] = -1
            numarr[i] = int(x[:-2]) ** expdic[x[-2]]
        else:
            numarr[i] = int(x[:-1]) ** expdic[x[-1]]

    for i in range(3):
        answer = answer + numarr[i] * starr[i] * starr[i + 1] * darr[i]

    return answer

res = "1D2S#10S"
print(solution(res))