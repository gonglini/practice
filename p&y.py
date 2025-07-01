# 문자열 내 p와 y의 개수

def solution(arr):
    cnt_p = 0
    cnt_y = 0

    for i in range(len(arr)):
        if arr[i] == "p" or arr[i] == "P":
            cnt_p += 1
        elif arr[i] == "y" or arr[i] == "Y":
            cnt_y += 1
       
    if cnt_p == cnt_y:
        return True
    else:
        return False

if __name__ == "__main__":
    arr = input("")
    print(solution(arr))
