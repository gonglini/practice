#시저 암호

import os 

def solution(s):
    result = []
    for i in range(len(s)):
        found = False
        for j in range(i - 1, -1, -1):  
            if s[i] == s[j]:
                result.append(i - j)
                found = True
                break
        if not found:
            result.append(-1)
    return result

if __name__ == "__main__":
    s = input()
    print(solution(s))

