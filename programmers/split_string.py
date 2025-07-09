#문자열 나누기

def solution(s):
    answer = 0
    first = ''
    same = diff = 0
    
    for c in s:
        if same == 0:
            first = c
            same = 1
        else:
            if c == first:
                same += 1
            else:
                diff += 1
        if same == diff:
            answer += 1
            same = diff = 0
    if same != 0:
        answer += 1
    return answer

if __name__ == "__main__":
    s = input().strip()
    print(solution(s))

