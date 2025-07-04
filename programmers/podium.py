#문자열 내 마음대로 정렬하기
import os 

def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    for i in range(len(strings)):
        answer.append(strings[i][1:])
    return answer


if __name__ == "__main__":
    strings = eval(input())
    n = int(input())
    print(solution(s,n))

