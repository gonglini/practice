#실패율
from collections import Counter

def solution(N, stages):
    answer = []
    counter = Counter(stages)
    total = len(stages)
    failure_list = []

    for stage in range(1, N + 1):
        if total != 0:
            count = counter[stage]
            failure = count / total
            failure_list.append((stage, failure))
            total -= count
        else:
            failure_list.append((stage, 0))

    failure_list.sort(key=lambda x: (-x[1], x[0]))

    for stage in failure_list:
        answer.append(stage[0])

    return answer

if __name__ == "__main__":
    N = int(input())
    stages = eval(input())
    print(solution(N, stages))

