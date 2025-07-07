#[1차] 비밀지도
import os 

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        or_result = arr1[i] | arr2[i]
        bin_str = bin(or_result)[2:].zfill(n)
        map_str = bin_str.replace('1', '#').replace('0', ' ')
        answer.append(map_str)
    return answer

if __name__ == "__main__":
    n = int(input())
    arr1 = eval(input())
    arr2 = eval(input())
    print(solution(n,arr1,arr2))
