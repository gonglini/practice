# 정수 내림차순으로 배치하기
def solution(num):
    num_list = list(str(num))               
    num_list.sort(reverse=True)             
    return int(''.join(num_list))  #join() : 리스트 내 요소를 순서대로 붙여서 하나의 문자열 생성      

if __name__ == "__main__":
    num = int(input(""))                   
    print(solution(num))
