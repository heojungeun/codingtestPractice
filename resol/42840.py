def solution(answers):
    each_ans = {1: [1, 2, 3, 4, 5],
                2: [2, 1, 2, 3, 2, 4, 2, 5],
                3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    order = [5, 8, 10]
    score = {1: 0, 2: 0, 3: 0}
    lena = len(answers)
    for i in range(lena):
        for j in range(3):
            if each_ans[j + 1][i % order[j]] == answers[i]:
                score[j + 1] += 1
    sortScore = sorted(score.items(), key=lambda x: (-x[1], x[0]))
    if sortScore[0][1] == sortScore[2][1]:
        return [1, 2, 3]
    elif sortScore[0][1] == sortScore[1][1]:
        return [sortScore[0][0], sortScore[1][0]]
    else:
        return [sortScore[0][0]]

def solution1(answers):
    answer = []
    each_ans = {1: [1, 2, 3, 4, 5],
                2: [2, 1, 2, 3, 2, 4, 2, 5],
                3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    order = [5, 8, 10]
    score = [0,0,0]
    lena = len(answers)
    for i in range(lena):
        for j in range(3):
            if each_ans[j + 1][i % order[j]] == answers[i]:
                score[j + 1] += 1
    maxs = max(score)
    for i in range(len(score)):
        if score[i] == maxs:
            answer.append(i+1)
    return answer

a = [1, 3, 2, 4, 2]
print(solution(a))
