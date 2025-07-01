#정수 제곱근 판별

def solution(num):
    if int(num ** 0.5) == num**0.5:
        return ((num ** 0.5)+1)**2
    else:
        return -1



if __name__ == "__main__":
    num = int(input(""))
    print(solution(num))
