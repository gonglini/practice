# 직사각형 별찍기
import os 

def solution(a,b):
    for i in range(0,b):
        print('*'*a)
   

if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    solution(a,b)
