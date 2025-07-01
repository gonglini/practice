# 두 정수 사이의 합
import os 

def solution(a,b):
    num =0
    if b < a:
        for i in range(b,a+1):
            num += i
    else:
        for i in range(a,b+1):
            num += i
    return num

if __name__ == "__main__":
    a, b= map(int,input("").split())
    print(solution(a,b))
