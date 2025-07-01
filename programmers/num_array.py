# 자연수 뒤집어 배열로 만들기

def solution(num):
    result = list(map(int, reversed(str(num))))  
    return result

if __name__ == "__main__":
    num = int(input("숫자를 입력하세요: "))
    print(solution(num))                        