# 3진법 뒤집기

import os 

def solution(num):
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, 3) 
        rev_base += str(mod)
    
    result = int(rev_base,3)
    return
    

if __name__ == "__main__":
    num = int(input(""))
    print(solution(num))
