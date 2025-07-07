#덧칠하기

import os 

def solution(n, m, section):
    section.sort()  
    result = 0
    i = 0

    while i < len(section):
        result += 1
        start = section[i]
        end = start + m - 1

        while i < len(section) and section[i] <= end:
            i += 1

    return result

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    section = eval(input())
    print(solution(n, m, section))


