# 서울에서 김서방 찾기
import os 

def solution(seoul):
    for idx, val in enumerate(seoul):
        if val == "Kim":
            return f"김서방은 {idx}에 있다"

if __name__ == "__main__":
    seoul = eval(input(""))
    print(solution(seoul))
