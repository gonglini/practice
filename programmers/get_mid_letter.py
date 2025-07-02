# 가운데 글자 가져오기

import os 

def solution(num):
    if len(num) % 2 == 0:
        return num[len(num)//2 -1 :len(num)//2+1]
    else:
        return num[len(num)//2 ]

if __name__ == "__main__":
    num = input("")
    print(solution(num))
