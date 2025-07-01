import os

def solution(num):
    ans = 0
    for i in str(num): #온라인 저지에서는 굳이 str로 변경 후해야함.
        ans += int(i)
    return ans

if __name__=="__main__":
    num = int(input(""))
    print(solution(num))