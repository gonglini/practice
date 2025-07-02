# 콜라츠 추측
import os 

def solution(num):
    cnt = 0
    while(cnt < 500):
        if num == 1:
            return cnt
        elif num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        cnt += 1
    return -1



if __name__ == "__main__":
    num = int(input(""))
    print(solution(num))
