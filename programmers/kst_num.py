#K번째수
import os 

def solution(a,c):
    result = []
    for i in c:
        tmp = a[i[0]-1:i[1]]
        tmp.sort()
        result.append(tmp[i[2]-1])
    return result


if __name__ == "__main__":
    arr = eval(input())
    command = eval(input())
    print(solution(arr, command))

