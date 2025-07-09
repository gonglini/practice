# 로또의 최고 순위와 최저 순위
import os 
from collections import Counter

def solution(lottos, win_nums):
    rank = 6
    num = 0
    answer = []
    cnt = Counter(lottos)
    for i in lottos:
        if i in win_nums:
            num+=1
    if num >=2:
        rank -=(num-1)
    else:
        pass
    max_rank=rank-cnt[0]
    if max_rank<1:
        max_rank =1
    else:
        pass
    answer.append(max_rank)
    answer.append(rank)
            

    return answer

if __name__ == "__main__":
    lottos = eval(input())
    win_nums = eval(input())
    print(solution(lottos,win_nums))

    '''
    def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = len(set(lottos) & set(win_nums))
    
    def get_rank(n):
        return 7 - n if n >= 2 else 6
    
    max_rank = get_rank(match_count + zero_count)
    min_rank = get_rank(match_count)
    
    return [max_rank, min_rank]

if __name__ == "__main__":
    lottos = eval(input())
    win_nums = eval(input())
    print(solution(lottos, win_nums))
'''
