# 약수의 개수와 덧셈
import os 

def solution(A, B):
    measure = []
    for i in range(A,B+1):
        cnt_measure=0
        for j in range(1,i+1):
            if i % j == 0:
                cnt_measure+=1
        if cnt_measure % 2 ==0:
            measure.append(i)
        else:
            measure.append(i*-1)   
    return sum(measure)


if __name__ == "__main__":
    A,B = map(int,input("").split())
    print(solution(A,B))
