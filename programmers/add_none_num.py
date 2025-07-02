#없는 숫자 더하기

def solution(num):
    result = 0
    for i in range(10):
        if i in num:
            pass
        else:
            result += i 
    return result

if __name__ == "__main__":
    num = input("")
    print(solution(num))                        