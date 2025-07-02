#문자열 다루기 기본
import os

def solution(arr):
    if len(arr) == 4 or len(arr) == 6:
        return (arr.isdigit()) #isdigit은 순자를 판별하느 메서드
    else:
        return False

if __name__=="__main__":
    arr = input("")
    print(solution(arr))