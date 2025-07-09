#완주하지 못한 선수
import os 
from collections import Counter

def solution(participant, completion):
    
    comp_counter = Counter(completion)

    result = []
    for num in participant:
        if comp_counter[num] > 0:
            comp_counter[num] -= 1  
        else:
            result.append(num)
    return ''.join(result)

if __name__ == "__main__":
    participant = eval(input())
    completion = eval(input())
    print(solution(participant, completion))
