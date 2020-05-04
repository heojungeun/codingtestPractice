def solution(people, limit):
    answer = 0
    people.sort()
    end=len(people)-1
    start=0
    while start < end:
        maxp = people[end]
        if limit-maxp >= people[start]:
            start += 1
        answer += 1
        end -= 1
    return answer

pe = [70,20,50,30,50]
li = 100
print(solution(pe,li))