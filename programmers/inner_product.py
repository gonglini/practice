# 내적
import os 

def solution(a,b):
    inner_product=0
    for i in range(len(a)):
        inner_product += a[i]*b[i]
    return inner_product

if __name__ == "__main__":
    a = eval(input(""))
    b = eval(input(""))
    print(solution(a,b))
