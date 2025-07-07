#명예의 전당 (1)
import os 

def solution(k, score):
    result = []
    honor = []
    for s in score:
        honor.append(s)
        honor.sort(reverse=True)
        if len(honor) > k:
            honor.pop()
        result.append(honor[-1])
    return result

if __name__ == "__main__":
    k = int(input())
    score = eval(input())
    print(solution(k, score))
