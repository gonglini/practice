#둘만의 암호

def solution(s, skip, index):

    answer = ''
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for _ in skip:
        alphabets = alphabets.replace(_, '')

    for ch in s:
        answer += alphabets[(alphabets.find(ch) + index) % len(alphabets)]

    return answer
if __name__ == "__main__":
    s = input("")
    skip = input("")
    index = int(input())
    print(solution(s,skip,index))
