# 두 개 뽑아서 더하기
import os 

def solution(s):
    result = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            result.add(s[i] + s[j])
    return sorted(result)

if __name__ == "__main__":
    s = eval(input())
    print(solution(s))


