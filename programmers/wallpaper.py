# 바탕화면 정리
import os 

def solution(wallpaper):    
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = -1, -1

    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                min_y = min(min_y, y)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                max_x = max(max_x, x)

    return [min_y, min_x, max_y + 1, max_x + 1]


if __name__ == "__main__":
    wallpaper = eval(input())   
    print(solution(wallpaper))
