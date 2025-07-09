#옹알이
import os

def solution(babbling):
    answer = 0

    babling = {'aya','woo','ye','ma'}  

    for i in babbling:
        prev_voca = ''  

        while True:
            if i[:3] in babling:
                if i[:3] == prev_voca: 
                    break  
                prev_voca = i[:3]
                i = i[3:]
            elif i[:2] in babling:
                if i[:2] == prev_voca:  
                    break  
                prev_voca = i[:2]
                i = i[2:]
            else:
                break

        if i == '':
            answer += 1

    return answer

if __name__ == "__main__":
    arr = eval(input())  
    print(solution(arr))
