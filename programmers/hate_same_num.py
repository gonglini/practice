# 직사각형 별찍기
import os 

def solution(arr):
    new_arr=[]
    for i in range(len(arr)):
        if i == 0:
            new_arr.append(arr[i])
        elif arr[i] == arr [i-1]:
            pass
        else:
            new_arr.append(arr[i])
    return new_arr
if __name__ == "__main__":
    arr= eval(input(""))
    print(solution(arr))
