# 수박수박수박수박수박수
import os 

def solution(num):
    return ("수박" * ((num//2)+1))[:num]


if __name__ == "__main__":
    num = int(input(""))
    print(solution(num))
