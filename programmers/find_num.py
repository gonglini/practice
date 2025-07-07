#소수찾기

import os 

def solution(n):
    ans = [True] * (n+1)
    ans[0] = ans[1] = False

    for i in range(2, int(n**0.5) + 1):
        if ans[i]:
            for j in range(i*i, n+1, i):  
                ans[j] = False

    return sum(ans)  

if __name__ == "__main__":
    n = int(input())
    print(solution(n))


