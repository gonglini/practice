#푸드 파이트 대회
import os 

def solution(s):
    answer = ""

    for i in range(1, len(s)):
        count = s[i] // 2
        answer += str(i) * count
    answer += "0"
    answer += answer[:-1][::-1]

    return answer


if __name__ == "__main__":
    s = eval(input())
    print(solution(s))

