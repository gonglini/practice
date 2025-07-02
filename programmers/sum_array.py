#행렬의 덧셈
import os

def solution(n, m):
    result = []
    for i in range(len(n)):             # 행 개수 기준 반복
        row = []
        for j in range(len(n[0])):      # 열 개수 기준 반복
            row.append(n[i][j] + m[i][j])
        result.append(row)
    return result

if __name__=="__main__":
    n =eval(input(""))
    m = eval(input(""))
    print(solution(n,m))