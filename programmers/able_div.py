# 나누어 떨어지는 숫자 배열
import os 

def solution(arr, divisor):
    result = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            result.append(arr[i])
    return sorted(result) if result else [-1]

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    divisor = int(input())
    print(solution(arr, divisor))
