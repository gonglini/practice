# 예산

import os 

def solution(d, budget):
    result = 0
    d.sort()
    for i in range(len(d)):
        budget-=d[i]
        if budget < 0:
            return result
        result +=1
    return result

if __name__ == "__main__":
    a = eval(input(""))
    b = int(input(""))
    print(solution(a, b))
