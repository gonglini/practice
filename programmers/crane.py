# 크레인 인형뽑기 게임
import os 

def solution(board, moves):
    result = []
    answer = 0

    stacks = []
    for i in range(len(board[0])):  # 열 인덱스
        stack = []
        for j in range(len(board)-1, -1, -1):  # 아래에서 위로
            if board[j][i] != 0:
                stack.append(board[j][i])
        stacks.append(stack)
    print(stacks)
    
    for move in moves:
        col_idx = move - 1
        if stacks[col_idx]:
            val = stacks[col_idx].pop()
            if result and result[-1] == val:
                result.pop()
                answer += 2
            else:
                result.append(val)
    
    return answer
    

if __name__ == "__main__":
    board = eval(input())   
    moves = eval(input()) 
    print(solution(board, moves))
