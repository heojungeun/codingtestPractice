def solution(priorities, location):
    answer = 0
    from queue import Queue
    q = Queue()
    for x in priorities:
        q.put(x)
    while True:
        maxp = max(priorities)
        tmp = q.get()
        if tmp < maxp:
            q.put(tmp)
            if location==0:
                location = q.qsize()-1
            else:
                location -= 1
        else:
            if location==0:
                answer += 1
                break
            else:
                priorities.remove(tmp)
                location -= 1
                answer += 1
    return answer

arr = [1, 1, 9, 1, 1, 1]
loc = 2
print(solution(arr, loc))