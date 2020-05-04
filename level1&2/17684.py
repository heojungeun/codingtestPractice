def solution(msg):
    answer = []
    dic = dict()
    alphalist = [chr(65+i) for i in range(26)]
    lenm = len(msg)
    for i, a in enumerate(alphalist):
        dic[a] = i+1
    leng, i, maxi = 0, 0, 26
    while True:
        leng += 1
        if not msg[i:i+leng] in dic:
            answer.append(dic[msg[i:i+leng-1]]) # w append
            maxi += 1
            dic[msg[i:i+leng]] = maxi
            i += leng-1
            leng = 0
        else:
            if i+leng-1 == lenm:
                answer.append(dic[msg[i:i+leng]])
                break
    return answer

def solution1(msg):
    answer = []
    dic = {chr(i+64):i for i in range(1, 27)}
    maxi = 27
    lenm = len(msg)
    while msg:
        leng = 1
        while msg[:leng] in dic.keys() and leng <= lenm:
            leng += 1
        leng -= 1
        if msg[:leng] in dic.keys():
            answer.append(dic[msg[:leng]])
            dic[msg[:leng+1]] = maxi
            maxi += 1
        msg = msg[leng:]
    return answer
mesg = "KAKAO"
print(solution(mesg))

