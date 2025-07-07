#폰켓몬
import os 
import random

def solution(nums):
    max_take = len(nums) // 2
    unique_types = len(set(nums))
    return min(unique_types, max_take)

if __name__ == "__main__":
    nums = eval(input())

    print(solution(nums))
