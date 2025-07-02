# 이상한 문자 만들기
import os 

def solution(s):
    result = []
    cnt = 0

    for c in s:
        if c == ' ':
            result.append(' ')
            cnt = 0  
        else:
            if cnt % 2 == 0:
                result.append(c.upper())
            else:
                result.append(c.lower())
            cnt+= 1

    return ''.join(result)

if __name__ == "__main__":
    s = input()
    print(solution(s))
