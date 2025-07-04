#가장 가까운 같은 글자
import os 

def solution(s, n):
    result = ''
    for c in s:
        if c == ' ':
            result += ' '
        elif c.isupper():
            result += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            result += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    return result


if __name__ == "__main__":
    s = input()
    n = int(input())
    print(solution(s, n))

