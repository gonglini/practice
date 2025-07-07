#기사단원의 무기
import os 
def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = 0
        j = 1
        while j * j <= i:
            if i % j == 0:
                if j * j == i:
                    cnt += 1
                else:
                    cnt += 2
            j += 1
        if cnt > limit:
            cnt = power
        answer += cnt
    return answer

if __name__ == "__main__":
    number = int(input())
    limit = int(input())
    power = int(input())
    print(solution(number, limit, power))
