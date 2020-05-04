#4
def solution(k, room_number):
    answer = []
    emt = [0]*k
    for x in room_number:
        if x in answer:
            i = emt.index(0, x)
            answer.append(i + 1)
            emt[i] = 1
        else:
            answer.append(x)
            emt[x-1] = 1
    return answer

rooms = 10
rn = [1,3,4,1,3,1]
print(solution(rooms,rn))