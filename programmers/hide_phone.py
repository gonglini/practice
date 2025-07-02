# 핸드폰 번호 가리기
import os 

def solution(num):
    num = "*" * (len(num) - 4) + num[-4:]
    return num

if __name__ == "__main__":
    num = input("")
    print(solution(num))
