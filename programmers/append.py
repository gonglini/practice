# x만큼 간격이 있는 n개의 숫자
import os 

def solution(a, b):
    result = []
    for i in range(b):
        result.append(a * (i + 1))
    return result

if __name__ == "__main__":
    a, b = map(int, input("").split())
    print(solution(a, b))
