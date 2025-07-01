#평균구하기

import os

def solution(arr):
    sum = 0
    for i in arr:
        sum += i
    result = sum / len(arr)
    return result


if __name__=="__main__":
    arr = list(map(int, input( "").split()))
    print(solution(arr))