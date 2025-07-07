#모의고사

import os 

def solution(answers):
    result = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for idx, ans in enumerate(answers):
        if ans == p1[idx % len(p1)]:
            scores[0] += 1
        if ans == p2[idx % len(p2)]:
            scores[1] += 1
        if ans == p3[idx % len(p3)]:
            scores[2] += 1

    max_score = max(scores)

    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)

    return result

if __name__ == "__main__":
    answers = eval(input())
    print(solution(answers))
