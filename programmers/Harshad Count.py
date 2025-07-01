#하샤드 수
import os

def solution(num):
    ans = 0
    for i in str(num): 
        ans += int(i)
    if num % ans == 0:
        return True
    else:
        return False

if __name__=="__main__":
    num = int(input(""))
    print(solution(num))