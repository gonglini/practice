#부족한 금액 계산하기
import os

def solution(price,money, count):
    total = 0
    for i in range(count+1):
        total += price*i
    result = -1*(money-total)
    if result < 0:
        result =0
    return result

if __name__=="__main__":
    price, money, count= map(int,input("").split())
    print(solution(price,money,count))