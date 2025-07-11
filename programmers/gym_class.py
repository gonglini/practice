#체육복

import os

def solution(n, lost, reserve):

    intersection = set(lost) & set(reserve)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)
    
    lost.sort()
    reserve.sort()
    
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)


if __name__=="__main__":
    num = int(input())
    lost =eval(input())
    reserve = eval(input())
    print(solution(num,lost,reserve))