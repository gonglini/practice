# 나머지가 1이 되는 수 찾기

import os 

def solution(num):
    count = 1
    while(True):
        if num % count == 1:
            return count
        else:
            count +=1

if __name__ == "__main__":
    num = int(input(""))
    print(solution(num))
