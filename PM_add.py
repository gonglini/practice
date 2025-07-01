#음양 더하기

import os

def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i]:  
            result += absolutes[i]
        else:         
            result -= absolutes[i]
    return result


if __name__ == "__main__":
    absolutes = list(map(int, input("").split()))
    signs = input("").split()  # "true false true"
    print(solution(absolutes, signs))
