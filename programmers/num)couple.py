#숫자 짝꿍
# 숫자 짝꿍
import os
from collections import Counter

def solution(X, Y):
    answer = ''
    x_counter = Counter(X)
    y_counter = Counter(Y)

    intersection = list((x_counter & y_counter).elements())
    intersection.sort(reverse=True)

    if not intersection:
        return "-1"
    if intersection[0] == '0':
        return "0"

    return ''.join(intersection)

if __name__ == "__main__":
    X = input()
    Y = input()
    print(solution(X, Y))
