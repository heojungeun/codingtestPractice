def solution1(operations):
    import heapq
    heap = []
    for x in operations:
        tmp = x.split(" ")
        if tmp[0] == "I":
            heapq.heappush(heap,int(tmp[1]))
        elif tmp[1] == "1":
            sortedheap = []
            while heap:
                sortedheap.append(heapq.heappop(heap))
            if sortedheap:
                sortedheap.pop()
                heap = sortedheap.copy()
        else:
            if heap:
                heapq.heappop(heap)
    sortedheap = []
    while heap:
        sortedheap.append(heapq.heappop(heap))
    if sortedheap:
        minh = sortedheap[0]
        maxh = sortedheap[-1]
        return [maxh, minh]
    return [0,0]

def solution(operations):
    import heapq
    heap = []
    for op in operations:
        x, y = op.split(" ")
        y = int(y)

        if x == "I":
            heapq.heappush(heap, y)
        elif heap:
            if y == -1:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
    if not heap:
        return [0,0]
    return [max(heap),heap[0]]

oper = ["I 7","I 5","I -5","D -1"]
print(solution(oper))