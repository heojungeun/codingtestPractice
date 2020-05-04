def solution(relation):
    answer = list()
    tupnum = len(relation)
    colnum = len(relation[0])
    for i in range(1 << colnum): # 부분집합 비트를 위해 필요한 반복
        tmpset = set()
        for j in range(tupnum): # 모든 튜플의 부분집합 스트링을 모으기 위해 반복
            tmp = ""
            for k in range(colnum):
                if i & (1<<k): # 부분집합 비트가 맞는지 확인
                    tmp += relation[j][k]
            tmpset.add(tmp)

        if len(tmpset) == tupnum: # 다르다면 유일성이 없는 키
            notdp = True
            for x in answer: # 최소성 검사
                if x & i == x:
                    notdp = False
            if notdp == True:
                answer.append(i)
    return len(answer)

rel = [["100","ryan","music","2"],
       ["200","apeach","math","2"],
       ["300","tube","computer","3"],
       ["400","con","computer","4"],
       ["500","muzi","music","3"],
       ["600","apeach","music","2"]]
print(solution(rel))