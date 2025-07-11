#햄버거 만들기
import os

def solution(ingredient):
    cnt = 0
    burger = [1, 2, 3, 1]
    while True:
        n = len(ingredient)
        m = len(burger)
        found = False
        for i in range(n - m + 1):
            if ingredient[i:i+m] == burger:
                ingredient = ingredient[:i] + ingredient[i+m:]  
                cnt += 1
                found = True
                break
        if not found:
            break
    return cnt

if __name__ == "__main__":
    ingredient = eval(input())
    print(solution(ingredient))
