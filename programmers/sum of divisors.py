def solution(num):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total += i
    return total

if __name__ == "__main__":
    n = int(input(""))
    solution(n)
