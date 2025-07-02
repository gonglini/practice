# 삼총사
import os 

def solution(num):
    cnt = 0 
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                if num[i]+num[j]+num[k] == 0:
                    cnt+=1
                else: 
                    pass
    return cnt

if __name__ == "__main__":
    num = eval(input(""))
    print(solution(num))
