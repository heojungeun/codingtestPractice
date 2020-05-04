def solution(record):
    answer = []
    dicid = {}
    tmp = []
    for x in record:
        listx = x.split(" ")
        if listx[0]=="Leave":
            tmp.append(listx[1]+"님이 나갔습니다.")
        else:
            if listx[0]=="Enter":
                tmp.append(listx[1]+"님이 들어왔습니다.")
            dicid[listx[1]] = listx[2]
    for x in tmp:
        listx = x.split("님")
        answer.append(dicid[listx[0]] + "님" + listx[1])
    return answer

rec = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(rec))