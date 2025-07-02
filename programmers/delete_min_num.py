# 제일 작은 수 제거하기

import os 

def solution(num):
    if len(num) == 1:
        return [-1]
    min_val = min(num)
    num.remove(min_val)
    return num

if __name__ == "__main__":
    num = eval(input(""))
    print(solution(num))
