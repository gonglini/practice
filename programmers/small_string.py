# 크기가 작은 부분문자열

import os 

def solution(t, p):
    len_p = len(p)
    p = int(p)
    count = 0

    for i in range(len(t) - len_p + 1):
        if int(t[i:i+len_p]) <= p:
            count += 1

    return count

if __name__ == "__main__":
    a, b = input().split(' ')
    print(solution(a, b))
