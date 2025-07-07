#추억 점수
import os 

def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        score = 0
        for j in range(len(name)):
            if name[j] in i:
                score += int(yearning[j])
        answer.append(score)
    return answer

if __name__ == "__main__":
    name = eval(input())
    yearning = eval(input())
    photo = eval(input())
    print(solution(name, yearning, photo))
