#콜라 문제
import os 

def solution(a,b,n):
    result = 0

    while(True):
        if n>= a:
            result += n//a*b
            n = n//a*b + n%a
            
        else:    
            return result


if __name__ == "__main__":
    a,b,n = map(int,input().split())
    print(solution(a,b,n))

