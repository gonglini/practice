#카드 뭉치
import os 

def solution(c1, c2, g):
    for word in g:
        if c1 and word == c1[0]:
            c1.pop(0)
        elif c2 and word == c2[0]:
            c2.pop(0)
        else:
            return "No"
    return "Yes"

if __name__ == "__main__":
    card1 = eval(input())
    card2 = eval(input())
    goal = eval(input())
    print(solution(card1, card2, goal))
