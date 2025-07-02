#문자열 내림차순으로 배치하기
import os

def solution(arr):
    return(''.join(reversed(sorted(arr))))

if __name__=="__main__":
    arr = eval(input(""))
    print(solution(arr))