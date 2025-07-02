# 최대공약수와 최소공배수
import os 

def solution(a,b):
    ans =[]
    c,d=a,b
    while b != 0:
        a, b = b, a % b
    ans.append(a)
    ans.append(c*d//a)
    return ans

if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    print(solution(a,b))
