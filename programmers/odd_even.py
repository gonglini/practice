#짝수와 홀수
import os

def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__=="__main__":
    num = int(input(""))
    print(solution(num))